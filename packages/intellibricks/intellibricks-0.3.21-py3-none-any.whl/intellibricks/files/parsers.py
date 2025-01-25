from __future__ import annotations

import abc
import tempfile
from typing import Optional, TypedDict

import msgspec
from architecture.data.files import RawFile
from architecture.utils.decorators import ensure_module_installed
from architecture.utils.functions import run_sync
from openai import OpenAI

from .constants import ParsingStrategy
from .parsed_files import PageContent, ParsedFile


class LocalSettings(TypedDict):
    use_gpu: bool


class FileParser(msgspec.Struct, frozen=True):
    """
    Abstract class for extracting content from files.
    This should be used as a base class for specific file parsers.
    """

    strategy: ParsingStrategy = ParsingStrategy.DEFAULT

    def extract_contents(
        self,
        file: RawFile,
    ) -> ParsedFile:
        """Extracts content from the file."""
        return run_sync(self.extract_contents_async, file)

    @abc.abstractmethod
    async def extract_contents_async(
        self,
        file: RawFile,
    ) -> ParsedFile:
        """Extracts content from the file."""
        raise NotImplementedError("This method should be implemented by subclasses.")


class IntellibricksFileParser(FileParser, frozen=True): ...


class PDFFileParser(IntellibricksFileParser, frozen=True): ...


class OfficeFileParser(IntellibricksFileParser, frozen=True): ...


class DocxFileParser(OfficeFileParser, frozen=True): ...


class PptxFileParser(OfficeFileParser, frozen=True): ...


class ExcelFileParser(OfficeFileParser, frozen=True): ...


class MarkitdownFileParser(FileParser, frozen=True):
    client: Optional[OpenAI] = None
    model: Optional[str] = None

    @ensure_module_installed("markitdown", "intellibricks[files]")
    async def extract_contents_async(
        self,
        file: RawFile,
    ) -> ParsedFile:
        from markitdown import MarkItDown
        from markitdown._markitdown import DocumentConverterResult

        match self.strategy:
            case (
                ParsingStrategy.DEFAULT | ParsingStrategy.MEDIUM | ParsingStrategy.FAST
            ):
                llm_client = None
                llm_model = None
            case ParsingStrategy.HIGH:
                llm_client = self.client or OpenAI()
                llm_model = self.model or "gpt-4o"

        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            temp_file.write(file.contents)
            temp_file.seek(0)
            converter = MarkItDown(llm_client=llm_client, llm_model=llm_model)
            result: DocumentConverterResult = converter.convert(temp_file.name)
            markdown: str = result.text_content

            # return a Document with one page only
            page_content = PageContent(
                page=1,
                text=markdown,
                md=markdown,
                images=[],
                items=[],
            )

            return ParsedFile(
                name=file.name,
                pages=[page_content],
            )
