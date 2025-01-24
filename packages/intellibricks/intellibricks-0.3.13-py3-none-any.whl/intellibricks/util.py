import inspect
import mimetypes
import os
import re
from copy import deepcopy
from pathlib import Path
from typing import Any, Callable, Literal, Union, Optional, cast, get_args, Mapping
from urllib.parse import urlparse

import msgspec
from architecture.logging import LoggerFactory
from typing_extensions import TypedDict

from intellibricks.llms.types import FileExtension

logger = LoggerFactory.create(__name__)


class CallerInfo(TypedDict):
    caller_class: Optional[str]
    caller_method: Optional[str]
    filename: Optional[str]
    line_number: Optional[int]
    caller_id: Optional[str]


def file_get_contents(filename: str) -> str:
    """
    Read the entire contents of a file and return it as a string.
    Supports various path scenarios and attempts to find the file
    even if only a partial path is provided.

    Args:
        filename (str): The path to the file to be read.

    Returns:
        str: The contents of the file as a string.

    Raises:
        FileNotFoundError: If the specified file cannot be found.
        IOError: If there's an error reading the file.
    """
    paths_to_try = [
        Path(filename),  # As provided
        Path(filename).resolve(),  # Absolute path
        Path(os.getcwd()) / filename,  # Relative to current working directory
        Path(os.path.dirname(inspect.stack()[1].filename))
        / filename,  # Relative to caller's directory
    ]

    for path in paths_to_try:
        try:
            return path.read_text()
        except FileNotFoundError:
            continue
        except IOError as e:
            raise IOError(f"Error reading file '{path}': {str(e)}")

    # If file not found, try to find it in the current directory structure
    current_dir = Path.cwd()
    filename_parts = Path(filename).parts

    for root, _, _ in os.walk(current_dir):
        root_path = Path(root)
        if all(part in root_path.parts for part in filename_parts[:-1]):
            potential_file = root_path / filename_parts[-1]
            if potential_file.is_file():
                try:
                    return potential_file.read_text()
                except IOError as e:
                    raise IOError(f"Error reading file '{potential_file}': {str(e)}")

    raise FileNotFoundError(
        f"File '{filename}' not found in any of the attempted locations."
    )


def markdown_to_html(markdown_text: str) -> str:
    # Create a Markdown instance with basic features including inline code
    # TODO(arthur): Implement this feature with no extra dependencies
    raise NotImplementedError("This feature is not yet implemented.")


def replace_placeholders(
    s: str, case_sensitive: bool = True, **replacements: Any
) -> str:
    """
    Replace placeholders in the format `{{key}}` within the string `s` with their corresponding values from `replacements`.

    Parameters:
        s (str): The input string containing placeholders.
        case_sensitive (bool, optional): If False, perform case-insensitive replacements. Defaults to True.
        **replacements: Arbitrary keyword arguments where each key corresponds to a placeholder in the string.

    Returns:
        str: The modified string with placeholders replaced by their corresponding values.

    Examples:
        >>> replace_placeholders("Hello, {{name}}!", name="Alice")
        'Hello, Alice!'

        >>> replace_placeholders(
        ...     "Dear {{title}} {{lastname}}, your appointment is on {{date}}.",
        ...     title="Dr.",
        ...     lastname="Smith",
        ...     date="Monday"
        ... )
        'Dear Dr. Smith, your appointment is on Monday.'

        >>> replace_placeholders(
        ...     "Coordinates: {{latitude}}, {{longitude}}",
        ...     latitude="40.7128° N",
        ...     longitude="74.0060° W"
        ... )
        'Coordinates: 40.7128° N, 74.0060° W'
    """
    return str_replace(
        s, replace_placeholders=True, case_sensitive=case_sensitive, **replacements
    )


def str_replace(
    s: str,
    *,
    case_sensitive: bool = True,
    use_regex: bool = False,
    count: int = -1,
    replace_placeholders: bool = False,
    **replacements: Any,
) -> str:
    """
    Replace multiple substrings in a string using keyword arguments, with additional options to modify behavior.

    Parameters:
        s (str): The input string on which to perform replacements.
        case_sensitive (bool, optional): If False, perform case-insensitive replacements. Defaults to True.
        use_regex (bool, optional): If True, treat the keys in replacements as regular expressions. Defaults to False.
        count (int, optional): Maximum number of occurrences to replace per pattern. Defaults to -1 (replace all).
        replace_placeholders (bool, optional): If True, replaces placeholders like '{{key}}' with their corresponding values. Defaults to False.
        **replacements: Arbitrary keyword arguments where each key is a substring or pattern to be replaced,
                        and each value is the replacement string.

    Returns:
        str: The modified string after all replacements have been applied.

    Examples:
        >>> str_replace("Hello, World!", Hello="Hi", World="Earth")
        'Hi, Earth!'

        >>> str_replace("The quick brown fox", quick="slow", brown="red")
        'The slow red fox'

        >>> str_replace("a b c d", a="1", b="2", c="3", d="4")
        '1 2 3 4'

        >>> str_replace("No changes", x="y")
        'No changes'

        >>> str_replace("Replace multiple occurrences", e="E", c="C")
        'REplaCE multiplE oCCurrEnCEs'

        >>> str_replace("Case Insensitive", case="CASE", case_sensitive=False)
        'CASE Insensitive'

        >>> str_replace(
        ...     "Use Regex: 123-456-7890",
        ...     use_regex=True,
        ...     pattern=r"\\d{3}-\\d{3}-\\d{4}",
        ...     replacement="PHONE"
        ... )
        'Use Regex: PHONE'

        >>> str_replace("Hello, {{name}}!", replace_placeholders=True, name="Alice")
        'Hello, Alice!'
    """

    # Determine the flags for regex based on case sensitivity
    flags = 0 if case_sensitive else re.IGNORECASE

    # Replace placeholders like {{key}} with their corresponding values
    if replace_placeholders:
        placeholder_pattern = r"\{\{(.*?)\}\}"

        def replace_match(match: re.Match[str]) -> str:
            key = match.group(1)
            if not case_sensitive:
                key_lookup = key.lower()
                replacements_keys = {k.lower(): k for k in replacements}
                if key_lookup in replacements_keys:
                    actual_key = replacements_keys[key_lookup]
                    value = replacements[actual_key]
                    return str(value)
                else:
                    string: str = match.group(0)
                    return string
            else:
                if key in replacements:
                    value = replacements[key]
                    return str(value)
                else:
                    string = match.group(0)
                    return string

        s = re.sub(placeholder_pattern, replace_match, s, flags=flags)

    # Now perform the standard replacements
    for old, new in replacements.items():
        if use_regex:
            s = re.sub(old, new, s, count=0 if count == -1 else count, flags=flags)
        else:
            if not case_sensitive:
                pattern = re.compile(re.escape(old), flags=flags)
                s = pattern.sub(new, s, count=0 if count == -1 else count)
            else:
                if count != -1:
                    s = s.replace(old, new, count)
                else:
                    s = s.replace(old, new)
    return s


def get_struct_from_schema(
    json_schema: dict[str, Any],
    *,
    bases: Optional[tuple[type[msgspec.Struct], ...]] = None,
    name: Optional[str] = None,
    module: Optional[str] = None,
    namespace: Optional[dict[str, Any]] = None,
    tag_field: Optional[str] = None,
    tag: Union[None, bool, str, int, Callable[[str], str | int]] = None,
    rename: Optional[
        Literal["lower", "upper", "camel", "pascal", "kebab"]
        | Callable[[str], Optional[str]]
        | Mapping[str, str]
    ] = None,
    omit_defaults: bool = False,
    forbid_unknown_fields: bool = False,
    frozen: bool = False,
    eq: bool = True,
    order: bool = False,
    kw_only: bool = False,
    repr_omit_defaults: bool = False,
    array_like: bool = False,
    gc: bool = True,
    weakref: bool = False,
    dict_: bool = False,
    cache_hash: bool = False,
) -> type[msgspec.Struct]:
    """
    Create a msgspec.Struct type from a JSON schema at runtime.

    If the schema contains local references ($ref = "#/..."), we
    resolve them recursively. The top-level must be an object schema
    with a "properties" field. Each property is turned into a struct
    field, with its "type" mapped into Python types.

    Returns a new Struct subclass.
    """

    def resolve_refs(node: Any, root_schema: dict[str, Any]) -> Any:
        """
        Recursively resolve local $ref references within `node`,
        using `root_schema` as the top-level reference container.
        """
        if isinstance(node, dict):
            node_dict = cast(dict[str, Any], node)  # <-- The crucial fix (type cast)
            if "$ref" in node_dict:
                ref_val: Any = node_dict["$ref"]
                if not isinstance(ref_val, str):
                    raise TypeError(
                        f"Expected $ref to be a string, got {type(ref_val)!r}."
                    )
                if not ref_val.startswith("#/"):
                    raise ValueError(
                        f"Only local references of the form '#/...'' are supported, got: {ref_val}"
                    )
                ref_path = ref_val.lstrip("#/")
                parts = ref_path.split("/")
                current: Any = root_schema
                for part in parts:
                    if not isinstance(current, dict):
                        raise TypeError(
                            "Encountered a non-dict node while traversing $ref path. "
                            f"Invalid path or schema content: {ref_val!r}"
                        )
                    if part not in current:
                        raise ValueError(
                            f"Reference {ref_val!r} cannot be resolved; key '{part}' not found."
                        )
                    current = current[part]
                return resolve_refs(current, root_schema)
            else:
                # Recurse into child values
                for k, v in list(node_dict.items()):
                    node_dict[k] = resolve_refs(v, root_schema)
                return node_dict

        elif isinstance(node, list):
            new_list: list[Any] = []
            for item in node:
                resolved_item = resolve_refs(item, root_schema)
                new_list.append(resolved_item)
            return new_list
        else:
            return node

    # 1) Resolve references
    resolved_schema = resolve_refs(json_schema, json_schema)

    # 2) Ensure the top-level result is a dict
    if not isinstance(resolved_schema, dict):
        raise TypeError(
            f"After reference resolution, the top-level schema is not a dict. Got: {type(resolved_schema)!r}"
        )

    # 3) top-level "type" must be "object"
    if "type" in resolved_schema:
        raw_type: Any = resolved_schema["type"]
        if not isinstance(raw_type, str):
            raise TypeError(
                f"Top-level 'type' should be a string, got {type(raw_type)!r}"
            )
        top_type = raw_type
    else:
        # If no "type" key, let's treat it as None or error
        top_type = None

    if top_type != "object":
        raise ValueError("JSON schema must define a top-level 'object' type.")

    # 4) "properties" must be a dict
    if "properties" not in resolved_schema:
        raise ValueError("JSON schema must define a 'properties' key at the top level.")

    raw_properties: dict[str, Any] = resolved_schema["properties"]
    if not isinstance(raw_properties, dict):
        raise ValueError(
            "JSON schema must define a 'properties' dict at the top level."
        )

    # 5) Derive struct name
    if name is None:
        if "title" in resolved_schema:
            schema_title = resolved_schema["title"]
            if isinstance(schema_title, str) and schema_title:
                name = schema_title
            else:
                name = "DynamicStruct"
        else:
            name = "DynamicStruct"

    # Ensure the name is a valid Python identifier (coarse):
    name = re.sub(r"\W|^(?=\d)", "_", name)

    # 6) Basic type mapping
    basic_type_map: dict[str, Any] = {
        "string": str,
        "integer": int,
        "number": float,
        "boolean": bool,
        "null": type(None),
    }

    # 7) Gather required fields
    if "required" in resolved_schema:
        r_val = resolved_schema["required"]
        if not isinstance(r_val, list):
            raise TypeError("'required' must be a list if present.")
        required_list = r_val
    else:
        required_list = []

    required_fields: list[str] = []
    for elem in required_list:
        if not isinstance(elem, str):
            raise TypeError(f"Found a non-string item in 'required': {elem!r}")
        required_fields.append(elem)

    # 8) Build up the fields
    fields: list[tuple[str, Any, Any]] = []

    for prop_name, prop_schema_any in raw_properties.items():
        if not isinstance(prop_name, str):
            raise TypeError(f"Property name must be a string, got {prop_name!r}")

        if not isinstance(prop_schema_any, dict):
            raise TypeError(
                f"Each property schema must be a dict, got {type(cast(object, prop_schema_any))!r} for '{prop_name}'"
            )
        prop_schema: dict[str, Any] = prop_schema_any

        # get 'type' from prop_schema
        if "type" in prop_schema:
            maybe_type = prop_schema["type"]
        else:
            maybe_type = None

        field_type: Any
        if maybe_type is None:
            # If there's no type in the property schema, just treat it as Any
            field_type = Any

        elif isinstance(maybe_type, str):
            if maybe_type == "array":
                # array -> items
                items_type_val: Any = None
                if "items" in prop_schema:
                    items_schema = prop_schema["items"]
                    if isinstance(items_schema, dict):
                        if "type" in items_schema:
                            it_val = items_schema["type"]
                            if isinstance(it_val, str):
                                items_type_val = basic_type_map.get(it_val, Any)
                            elif isinstance(it_val, list):
                                sub_union: list[Any] = []
                                for sub_t in it_val:
                                    if isinstance(sub_t, str):
                                        sub_union.append(basic_type_map.get(sub_t, Any))
                                    else:
                                        sub_union.append(Any)
                                if len(sub_union) == 1:
                                    items_type_val = sub_union[0]
                                else:
                                    items_type_val = Union[tuple(sub_union)]
                            else:
                                items_type_val = Any
                        else:
                            items_type_val = Any
                    else:
                        items_type_val = Any
                else:
                    items_type_val = Any
                field_type = list[items_type_val]
            else:
                if maybe_type in basic_type_map:
                    field_type = basic_type_map[maybe_type]
                elif maybe_type == "object":
                    field_type = dict[str, Any]
                else:
                    field_type = Any

        elif isinstance(maybe_type, list):
            # handle union of possible types
            union_members: list[Any] = []
            for t_ in maybe_type:
                if not isinstance(t_, str):
                    union_members.append(Any)
                    continue
                if t_ == "array":
                    arr_item_type: Any = Any
                    if "items" in prop_schema:
                        arr_items = prop_schema["items"]
                        if isinstance(arr_items, dict):
                            if "type" in arr_items:
                                arr_it_type = arr_items["type"]
                                if isinstance(arr_it_type, str):
                                    arr_item_type = basic_type_map.get(arr_it_type, Any)
                                elif isinstance(arr_it_type, list):
                                    sub_union2: list[Any] = []
                                    for st in arr_it_type:
                                        if isinstance(st, str):
                                            sub_union2.append(
                                                basic_type_map.get(st, Any)
                                            )
                                        else:
                                            sub_union2.append(Any)
                                    arr_item_type = Union[tuple(sub_union2)]
                    union_members.append(list[arr_item_type])
                elif t_ in basic_type_map:
                    union_members.append(basic_type_map[t_])
                elif t_ == "object":
                    union_members.append(dict[str, Any])
                else:
                    union_members.append(Any)

            if len(union_members) == 1:
                field_type = union_members[0]
            else:
                field_type = Union[tuple(union_members)]
        else:
            field_type = Any

        # default
        if prop_name in required_fields:
            default_val: Any = msgspec.NODEFAULT
        else:
            if "default" in prop_schema:
                default_val = prop_schema["default"]
            else:
                default_val = msgspec.NODEFAULT

        fields.append((prop_name, field_type, default_val))

    struct_type = msgspec.defstruct(
        name=name,
        fields=fields,
        bases=bases,
        module=module,
        namespace=namespace,
        tag=tag,
        tag_field=tag_field,
        rename=rename,
        omit_defaults=omit_defaults,
        forbid_unknown_fields=forbid_unknown_fields,
        frozen=frozen,
        eq=eq,
        order=order,
        kw_only=kw_only,
        repr_omit_defaults=repr_omit_defaults,
        array_like=array_like,
        gc=gc,
        weakref=weakref,
        dict=dict_,
        cache_hash=cache_hash,
    )

    return struct_type


def fix_broken_json(
    string: str, *, decoder: msgspec.json.Decoder[dict[str, Any]]
) -> dict[str, Any]:
    """
    Parses a python object (JSON) into an instantiated Python dictionary, applying automatic corrections for common formatting issues.

    This function attempts to extract JSON objects from a string containing JSON data possibly embedded within other text. It handles JSON strings that may be embedded within code block markers (e.g., Markdown-style ```json code blocks) and applies a series of fix-up functions to correct common JSON formatting issues such as unescaped characters, missing commas, and control characters that may prevent successful parsing.

    Parameters
    ----------
    string : str
        The string containing JSON string to deserialize. This may include code block markers, surrounding text, and may have minor formatting issues.

    Returns
    -------
    dict[str, Any]
        A Python dictionary representing the parsed JSON string.

    Raises
    ------
    ValueError
        If no JSON object could be found in the string, or if parsing fails after applying all fix functions.

    Examples
    --------
    Extracting JSON from text with embedded JSON:

        >>> json_str = 'Sure! Here is your formatted json:\\n\\n```json\\n{"name": "Alice", "age": 30}\\n```'
        >>> fix_broken_json(json_str)
        {'name': 'Alice', 'age': 30}

        >>> json_str = '{ "name": "Bob", "age": 25 }'
        >>> fix_broken_json(json_str)
        {'name': 'Bob', 'age': 25}

        >>> json_str = 'Here is the json\\n\\n{ "name": "Charlie", "age": 28 }'
        >>> fix_broken_json(json_str)
        {'name': 'Charlie', 'age': 28}

        >>> json_str = '{ "name": "David", "age": 35 }\\n\\nI provided the json above'
        >>> fix_broken_json(json_str)
        {'name': 'David', 'age': 35}

    Basic usage:

        >>> json_str = '{"name": "Alice", "age": 30}'
        >>> fix_broken_json(json_str)
        {'name': 'Alice', 'age': 30}

    Handling code block markers:

        >>> json_str = '''
        ... ```json
        ... {
        ...     "name": "Bob",
        ...     "age": 25
        ... }
        ... ```
        ... '''
        >>> fix_broken_json(json_str)
        {'name': 'Bob', 'age': 25}

    Handling unescaped backslashes:

        >>> json_str = '{"path": "C:\\Users\\Bob"}'
        >>> deserialize_json(json_str)
        {'path': 'C:\\Users\\Bob'}

    Handling unescaped newlines within strings:

        >>> json_str = '{"text": "Line1\nLine2"}'
        >>> deserialize_json(json_str)
        {'text': 'Line1\\nLine2'}

    Handling missing commas between objects in an array:

        >>> json_str = '{"items": [{"id": 1} {"id": 2}]}'
        >>> deserialize_json(json_str)
        {'items': [{'id': 1}, {'id': 2}]}

    Removing control characters:

        >>> json_str = '{"text": "Hello\\x00World"}'
        >>> deserialize_json(json_str)
        {'text': 'HelloWorld'}

    Attempting to parse invalid JSON:

        >>> json_str = 'Not a JSON string'
        >>> deserialize_json(json_str)
        Traceback (most recent call last):
            ...
        ValueError: No JSON object could be found in the content.

    Parsing fails after all fixes:

        >>> json_str = '{"name": "David", "age": }'
        >>> deserialize_json(json_str)
        Traceback (most recent call last):
            ...
        ValueError: Failed to parse JSON content after multiple attempts.


    Notes
    -----
    The function applies a series of fix functions to correct common issues that may prevent JSON parsing. The fix functions applied are:

    - **No fix**: Attempts to parse the string as-is.
    - **Escaping unescaped backslashes**: Fixes unescaped backslashes in the string.
    - **Escaping unescaped newlines within strings**: Escapes unescaped newline and carriage return characters within JSON strings.
    - **Inserting missing commas between JSON objects in arrays**: Inserts missing commas between JSON objects in arrays.
    - **Removing control characters**: Removes control characters that may interfere with JSON parsing.
    - **Removing invalid characters**: Removes any remaining invalid characters (non-printable ASCII characters).

    If parsing fails after all fixes, a `ValueError` is raised.

    Dependencies
    ------------
    - **msgspec**: Used for JSON decoding. Install via `pip install msgspec`.
    - **re**: Used for regular expression operations.
    - **logging**: Used for logging errors during parsing attempts.

    """

    # Remove code block markers if present
    string = re.sub(r"^```(?:json)?\n", "", string, flags=re.IGNORECASE | re.MULTILINE)
    string = re.sub(r"\n```$", "", string, flags=re.MULTILINE)

    # Helper function to find substrings with balanced braces
    def find_json_substrings(s: str) -> list[str]:
        substrings: list[str] = []
        stack: list[str] = []
        start: Optional[int] = None
        for i, c in enumerate(s):
            if c == "{":
                if not stack:
                    # Potential start of JSON object
                    start = i
                stack.append(c)
            elif c == "}":
                if stack:
                    stack.pop()
                    if not stack and start is not None:
                        # Potential end of JSON object
                        end = i + 1  # Include the closing brace
                        substrings.append(s[start:end])
                        start = None  # Reset start
        return substrings

    # Find all potential JSON substrings
    json_substrings: list[str] = find_json_substrings(string)

    if not json_substrings:
        raise ValueError("No JSON object could be found in the string.")

    # Initialize variables for parsing attempts
    parsed_obj: dict[str, Any]

    # Define fix functions as inner functions
    def _fix_unescaped_backslashes(input_string: str) -> str:
        """
        Fix unescaped backslashes by escaping them.

        Args:
            input_string (str): The JSON string to fix.

        Returns:
            str: The fixed JSON string.
        """
        return re.sub(r'(?<!\\)\\(?![\\"])', r"\\\\", input_string)

    def _escape_unescaped_newlines(input_string: str) -> str:
        """
        Escape unescaped newline and carriage return characters within JSON strings.

        Args:
            input_string (str): The JSON string to fix.

        Returns:
            str: The fixed JSON string.
        """
        # Pattern to find JSON strings
        string_pattern = r'"((?:\\.|[^"\\])*)"'

        def replace_newlines_in_string(match: re.Match[str]) -> str:
            content_inside_quotes = match.group(1)
            # Escape unescaped newlines and carriage returns
            content_inside_quotes = content_inside_quotes.replace("\n", "\\n").replace(
                "\r", "\\r"
            )
            return f'"{content_inside_quotes}"'

        fixed_content = re.sub(
            string_pattern, replace_newlines_in_string, input_string, flags=re.DOTALL
        )
        return fixed_content

    def _insert_missing_commas(input_string: str) -> str:
        """
        Insert missing commas between JSON objects in arrays.

        Args:
            input_string (str): The JSON string to fix.

        Returns:
            str: The fixed JSON string.
        """
        # Insert commas between closing and opening braces/brackets
        patterns = [
            (r"(\})(\s*\{)", r"\1,\2"),  # Between } and {
            (r"(\])(\s*\[)", r"\1,\2"),  # Between ] and [
            (r"(\])(\s*\{)", r"\1,\2"),  # Between ] and {
            (r"(\})(\s*\[)", r"\1,\2"),  # Between } and [
        ]
        fixed_content = input_string
        for pattern, replacement in patterns:
            fixed_content = re.sub(pattern, replacement, fixed_content)
        return fixed_content

    def _remove_control_characters(input_string: str) -> str:
        """
        Remove control characters that may interfere with JSON parsing.

        Args:
            input_string (str): The JSON string to fix.

        Returns:
            str: The fixed JSON string.
        """
        return "".join(c for c in input_string if c >= " " or c == "\n")

    def _remove_invalid_characters(input_string: str) -> str:
        """
        Remove any remaining invalid characters (non-printable ASCII characters).

        Args:
            input_string (str): The JSON string to fix.

        Returns:
            str: The fixed JSON string.
        """
        return re.sub(r"[^\x20-\x7E]+", "", input_string)

    # Define a list of fix functions
    fix_functions: list[Callable[[str], str]] = [
        lambda x: x,  # First attempt without any fixes
        _fix_unescaped_backslashes,
        _escape_unescaped_newlines,
        _insert_missing_commas,
        _remove_control_characters,
        _remove_invalid_characters,
    ]

    # Attempt parsing for each JSON substring, applying fixes sequentially
    for json_content in json_substrings:
        for fix_func in fix_functions:
            try:
                # Apply the fix function
                fixed_content: str = fix_func(json_content)
                # Try parsing the JSON string
                parsed_obj = decoder.decode(fixed_content)
                return parsed_obj
            except (msgspec.DecodeError, ValueError) as e:
                logger.error(
                    f"Failed to parse JSON string after applying fix: {fix_func.__name__}"
                )
                logger.error(f"Exception: {e}")
                continue  # Try next fix function
        # If parsing fails for this substring, continue to next
        continue

    # If all attempts fail, raise an error
    raise ValueError("Failed to parse JSON string after multiple attempts.")


def is_url(url: str) -> bool:
    """
    Check if a string is a valid URL.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def struct_to_dict(struct: msgspec.Struct) -> dict[str, Any]:
    return msgspec.json.decode(msgspec.json.encode(struct), type=dict)


def dict_to_struct[S: msgspec.Struct](d: dict[str, Any], struct: type[S]) -> S:
    return msgspec.json.decode(msgspec.json.encode(d), type=struct)


def flatten_msgspec_schema(
    schema: dict[str, Any],
    remove_parameters: Optional[list[str]] = None,
    openai_like: bool = False,
) -> dict[str, Any]:
    """
    A function that flattens msgspec's JSON schema into a OpenAPI3.0–compliant schema.
    Specifically:
      1. Inlines $ref from $defs, removes $defs.
      2. Removes specified parameters (title, examples, etc.).
      3. Converts anyOf=[{type:null},{type:X}] -> {type:X, nullable:true}.
      4. If anyOf remains and has more than 1 branch, remove all sibling fields,
         so the node only has {"anyOf": [...]} (Vertex's constraint).
      5. Ensures each node not in an anyOf has a valid "type" if it's an object/array/string.
      6. If openai_like=True, sets "additionalProperties": false for "type=object".
      7. Wraps raw string properties so they become { "type": "string" } if needed.

    This handles the error:
      "Unable to submit request because one or more response schemas specified
       other fields alongside any_of. When using any_of, it must be the only field set."
    """

    # Copy the input so we don't mutate the original
    schema_copy = deepcopy(schema)

    # Our local store of $defs (if any)
    defs: dict[str, Any] = {}

    # 1) Extract $defs
    if "$defs" in schema_copy:
        raw_defs = schema_copy.pop("$defs")
        if not isinstance(raw_defs, dict):
            raise TypeError(f"Expected $defs to be a dict, got {type(raw_defs)!r}")
        defs = raw_defs

    # region --- Helper Functions ---

    def resolve_references(
        node: None | bool | int | float | str | list[Any] | dict[str, Any],
    ) -> None | bool | int | float | str | list[Any] | dict[str, Any]:
        """Inline references, remove unwanted parameters, recurse."""
        if isinstance(node, dict):
            # inline $ref
            if "$ref" in node:
                ref_val = node["$ref"]
                if not isinstance(ref_val, str):
                    raise TypeError(f"$ref must be a string, got {type(ref_val)!r}")
                ref_name = ref_val.split("/")[-1]
                if ref_name not in defs:
                    raise ValueError(f"Ref {ref_name!r} not found in $defs.")
                inlined = deepcopy(defs[ref_name])
                return resolve_references(inlined)

            # handle anyOf by resolving each item
            if "anyOf" in node:
                any_of_val = node["anyOf"]
                if isinstance(any_of_val, list):
                    new_anyof = []
                    for sub in any_of_val:
                        """
                        Type of "append" is partially unknown
                        Type of "append" is "(object: Unknown, /) -> None"PylancereportUnknownMemberType
                        (variable) new_anyof: list[Unknown]
                        """
                        """
                        Argument type is unknown
                        Argument corresponds to parameter "node" in function "resolve_references"PylancereportUnknownArgumentType
                        (variable) sub: Unknown
                        """
                        new_anyof.append(resolve_references(sub))  # type: ignore
                    node["anyOf"] = new_anyof

            # remove specified parameters
            if remove_parameters is not None:
                for p in remove_parameters:
                    if p in node:
                        node.pop(p)

            # recurse into children
            for _k, v in list(node.items()):
                # don't re-handle anyOf if we already replaced it
                if _k != "anyOf":
                    node[_k] = resolve_references(v)

            return node

        elif isinstance(node, list):
            new_list = []
            for i in node:
                """
                Type of "append" is partially unknown
                Type of "append" is "(object: Unknown, /) -> None"PylancereportUnknownMemberType
                (method) def append(
                    object: Unknown,
                    /
                ) -> None
                Append object to the end of the list.
                """
                new_list.append(resolve_references(i))  # type: ignore
            return new_list

        else:
            # None, bool, int, float, str
            return node

    def convert_optional_to_nullable(
        n: None | bool | int | float | str | list[Any] | dict[str, Any],
    ) -> None | bool | int | float | str | list[Any] | dict[str, Any]:
        """
        Convert a 2-item anyOf with one null and one non-null
        => {type: X, nullable: true}
        """
        if isinstance(n, dict):
            any_of_val = n.get("anyOf")
            if isinstance(any_of_val, list):
                """
                Argument type is partially unknown
                Argument corresponds to parameter "obj" in function "len"
                Argument type is "list[Unknown]"PylancereportUnknownArgumentType
                (variable) any_of_val: list[Unknown]
                """
                if len(any_of_val) == 2:  # type: ignore
                    # check if exactly one is {"type": "null"}
                    types_collected: list[Optional[str]] = []
                    for sub in any_of_val:
                        if isinstance(sub, dict):
                            """
                            Type of "get" is partially unknown
                            Type of "get" is "Overload[(key: Unknown, /) -> (Unknown | None), (key: Unknown, default: Unknown, /) -> Unknown, (key: Unknown, default: _T@get, /) -> (Unknown | _T@get)]"PylancereportUnknownMemberType
                            (variable) sub: dict[Unknown, Unknown]
                            """
                            t = sub.get("type")  # type: ignore
                            if isinstance(t, str):
                                types_collected.append(t)
                            else:
                                types_collected.append(None)
                        else:
                            types_collected.append(None)
                    # e.g. types_collected might be ["null", "string"]

                    distinct_types = {typ for typ in types_collected if typ is not None}
                    if (
                        "null" in types_collected
                        and len(distinct_types - {"null"}) == 1
                    ):
                        null_idx = types_collected.index("null")
                        nonnull_idx = 1 - null_idx
                        nonnull_sub = any_of_val[nonnull_idx]
                        if (
                            isinstance(nonnull_sub, dict)
                            and "type" in nonnull_sub
                            and isinstance(nonnull_sub["type"], str)
                        ):
                            # flatten
                            n["type"] = nonnull_sub["type"]
                            n["nullable"] = True
                            """
                            Argument type is partially unknown
                            Argument corresponds to parameter "iterable" in function "__init__"
                            Argument type is "dict_items[Unknown, Unknown]"PylancereportUnknownArgumentType
                            (variable) nonnull_sub: dict[Unknown, Unknown]
                            """
                            for key, val in list(nonnull_sub.items()):  # type: ignore
                                if key != "type":
                                    n[key] = val
                            n.pop("anyOf", None)
                else:
                    new_anyof = []
                    for s in any_of_val:
                        """
                        Type of "append" is partially unknown
                        Type of "append" is "(object: Unknown, /) -> None"PylancereportUnknownMemberType
                        (method) def append(
                            object: Unknown,
                            /
                        ) -> None
                        Append object to the end of the list.
                        """
                        new_anyof.append(convert_optional_to_nullable(s))  # type: ignore
                    n["anyOf"] = new_anyof

            # deeper recursion
            for _k, v in list(n.items()):
                if _k != "anyOf":
                    n[_k] = convert_optional_to_nullable(v)
            return n

        elif isinstance(n, list):
            return [convert_optional_to_nullable(x) for x in n]

        else:
            return n

    def remove_siblings_if_anyof(
        n: None | bool | int | float | str | list[Any] | dict[str, Any],
    ) -> None | bool | int | float | str | list[Any] | dict[str, Any]:
        """
        Vertex AI constraint: If anyOf is present, it must be the *only* key in that dict node.
        We'll remove 'type', 'properties', 'nullable', etc. if anyOf is found.
        """
        if isinstance(n, dict):
            any_of_val = n.get("anyOf")
            if isinstance(any_of_val, list):
                # If there's at least 1 item in anyOf, strip out all sibling fields
                """
                Argument type is partially unknown
                Argument corresponds to parameter "obj" in function "len"
                Argument type is "list[Unknown]"PylancereportUnknownArgumentType
                (variable) any_of_val: list[Unknown]
                """
                if len(any_of_val) >= 1:  # type: ignore
                    # remove all siblings except "anyOf"
                    keep = {"anyOf"}
                    for k_to_delete in list(n.keys()):
                        if k_to_delete not in keep:
                            n.pop(k_to_delete)
                    # Recurse into each sub-branch
                    new_anyof = []
                    for x in any_of_val:
                        """
                        Type of "append" is partially unknown
                        Type of "append" is "(object: Unknown, /) -> None"PylancereportUnknownMemberType
                        (method) def append(
                            object: Unknown,
                            /
                        ) -> None
                        Append object to the end of the list.
                        """
                        new_anyof.append(remove_siblings_if_anyof(x))  # type: ignore
                    n["anyOf"] = new_anyof
                    return n

            # else no anyOf or it's not a list => keep recursing
            for _k, v in list(n.items()):
                n[_k] = remove_siblings_if_anyof(v)
            return n

        elif isinstance(n, list):
            return [remove_siblings_if_anyof(x) for x in n]

        else:
            return n

    def enforce_no_additional_props(
        n: None | bool | int | float | str | list[Any] | dict[str, Any],
    ) -> None:
        """If openai_like, set additionalProperties=false on all object nodes."""
        if isinstance(n, dict):
            node_type = n.get("type")
            if node_type == "object":
                if "additionalProperties" not in n:
                    n["additionalProperties"] = False
            for val in n.values():
                enforce_no_additional_props(val)
        elif isinstance(n, list):
            for item in n:
                enforce_no_additional_props(item)

    def ensure_type_fields(
        n: None | bool | int | float | str | list[Any] | dict[str, Any],
    ) -> None:
        """
        For nodes that do *not* have anyOf, ensure they have a "type".
        If they have "properties" => object
        If they have "items" => array
        Else => string (or if "enum"/"format"/"pattern", => string).
        """
        if isinstance(n, dict):
            # If node has anyOf, skip forcing type
            if "anyOf" in n:
                any_of_val = n["anyOf"]
                if isinstance(any_of_val, list):
                    for item in any_of_val:
                        """
                        Argument type is unknown
                        Argument corresponds to parameter "n" in function "ensure_type_fields"PylancereportUnknownArgumentType
                        (variable) item: Unknown
                        """
                        ensure_type_fields(item)  # type: ignore
                return

            node_type = n.get("type")
            if not isinstance(node_type, str):
                if "properties" in n:
                    n["type"] = "object"
                elif "items" in n:
                    n["type"] = "array"
                elif any(k in n for k in ("enum", "format", "pattern")):
                    n["type"] = "string"
                else:
                    n["type"] = "string"

            # unify if properties => type=object
            if "properties" in n and n.get("type") != "object":
                n["type"] = "object"
            # unify if items => type=array
            if "items" in n and n.get("type") != "array":
                n["type"] = "array"

            for _k, v in list(n.items()):
                ensure_type_fields(v)

        elif isinstance(n, list):
            for item in n:
                ensure_type_fields(item)

    def wrap_raw_string_in_type(
        n: None | bool | int | float | str | list[Any] | dict[str, Any],
    ) -> None:
        """
        If in n["properties"], we find a raw string => convert it to {"type": "string"} etc.
        """
        if isinstance(n, dict):
            props = n.get("properties")
            if isinstance(props, dict):
                """
                Argument type is partially unknown
                Argument corresponds to parameter "iterable" in function "__init__"
                Argument type is "dict_items[Unknown, Unknown]"PylancereportUnknownArgumentType
                (method) def items() -> dict_items[Unknown, Unknown]
                """
                for prop_key, prop_val in list(props.items()):  # type: ignore
                    if isinstance(prop_val, str):
                        props[prop_key] = {"type": prop_val}
                    elif isinstance(prop_val, (int, float, bool)):
                        props[prop_key] = {"type": "string"}

            it = n.get("items")
            if isinstance(it, str):
                n["items"] = {"type": it}

            for _k, v in list(n.items()):
                wrap_raw_string_in_type(v)

        elif isinstance(n, list):
            for item in n:
                wrap_raw_string_in_type(item)
        else:
            # None, bool, int, float, str
            pass

    # endregion --- Helper Functions ---

    # ---------------
    # Core Execution
    # ---------------

    # A) Inline refs, remove params
    flattened = resolve_references(schema_copy)

    # B) Convert optional 2-item anyOf => type, nullable
    flattened = convert_optional_to_nullable(flattened)

    # C) Remove siblings if there's an anyOf left
    flattened = remove_siblings_if_anyof(flattened)

    # D) If openai_like, enforce no additional props
    if openai_like:
        enforce_no_additional_props(flattened)

    # E) Ensure type fields for nodes not in anyOf
    ensure_type_fields(flattened)

    # F) Wrap raw string properties => {"type": "string"}
    wrap_raw_string_in_type(flattened)

    # We began with "dict[str, ...]" at the top,
    # but it might theoretically have become a list if the user had a weird $ref
    # that points to a list. Safeguard:
    if not isinstance(flattened, dict):
        raise TypeError(
            "flatten_msgspec_schema ended with a top-level non-dict. "
            "Check your references or schema structure."
        )

    return flattened


def is_file_url(url: str) -> bool:
    """
    Check if a URL is a file URL based on its extension.

    Parameters:
        url (str): The URL to check.

    Returns:
        bool: True if the URL ends with a known file extension, False otherwise.
    """
    # Parse the URL to extract the path
    parsed_url = urlparse(url)
    path = parsed_url.path

    # Guess the MIME type based on the file extension
    mime_type, _ = mimetypes.guess_type(path)

    # If a MIME type is found, the URL likely points to a file
    return mime_type is not None


def get_file_extension(url: str) -> FileExtension:
    """
    Get the file extension from a URL.

    Parameters:
        url (str): The URL to extract the file extension from.

    Returns:
        str: The file extension (e.g., '.txt', '.jpg') extracted from the URL.
    """
    extension = url[url.rfind(".") :]
    if extension not in get_args(FileExtension):
        raise ValueError(f"Unsupported file extension: {extension}")

    return cast(FileExtension, extension)
