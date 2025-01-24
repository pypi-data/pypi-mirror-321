from __future__ import annotations

from typing import Literal, TypeAlias

FileExtension: TypeAlias = Literal[
    ".jpeg",
    ".jpg",
    ".png",
    ".gif",
    ".mp3",
    ".wav",
    ".mp4",
    ".avi",
    ".mov",
    ".webm",
]
GenAIModelType: TypeAlias = Literal[
    "google/genai/gemini-1.5-flash",
    "google/genai/gemini-1.5-flash-8b",
    "google/genai/gemini-1.5-flash-001",
    "google/genai/gemini-1.5-flash-002",
    "google/genai/gemini-1.5-pro",
    "google/genai/gemini-1.5-pro-001",
    "google/genai/gemini-1.0-pro-002",
    "google/genai/gemini-1.5-pro-002",
    "google/genai/gemini-flash-experimental",
    "google/genai/gemini-pro-experimental",
    "google/genai/gemini-2.0-flash-exp",
]

VertexAIModelType: TypeAlias = Literal[
    "google/vertexai/gemini-2.0-flash-exp",
    "google/vertexai/gemini-1.5-flash",
    "google/vertexai/gemini-1.5-flash-8b",
    "google/vertexai/gemini-1.5-flash-001",
    "google/vertexai/gemini-1.5-flash-002",
    "google/vertexai/gemini-1.5-pro",
    "google/vertexai/gemini-1.5-pro-001",
    "google/vertexai/gemini-1.0-pro-002",
    "google/vertexai/gemini-1.5-pro-002",
    "google/vertexai/gemini-flash-experimental",
    "google/vertexai/gemini-pro-experimental",
]

GoogleModelType: TypeAlias = Literal[
    GenAIModelType,
    VertexAIModelType,
]

OpenAIModelType: TypeAlias = Literal[
    "openai/api/o1",
    "openai/api/o1-2024-12-17",
    "openai/api/o1-preview",
    "openai/api/o1-preview-2024-09-12",
    "openai/api/o1-mini",
    "openai/api/o1-mini-2024-09-12",
    "openai/api/gpt-4o",
    "openai/api/gpt-4o-2024-11-20",
    "openai/api/gpt-4o-2024-08-06",
    "openai/api/gpt-4o-2024-05-13",
    "openai/api/gpt-4o-audio-preview",
    "openai/api/gpt-4o-audio-preview-2024-10-01",
    "openai/api/gpt-4o-audio-preview-2024-12-17",
    "openai/api/gpt-4o-mini-audio-preview",
    "openai/api/gpt-4o-mini-audio-preview-2024-12-17",
    "openai/api/chatgpt-4o-latest",
    "openai/api/gpt-4o-mini",
    "openai/api/gpt-4o-mini-2024-07-18",
    "openai/api/gpt-4-turbo",
    "openai/api/gpt-4-turbo-2024-04-09",
    "openai/api/gpt-4-0125-preview",
    "openai/api/gpt-4-turbo-preview",
    "openai/api/gpt-4-1106-preview",
    "openai/api/gpt-4-vision-preview",
    "openai/api/gpt-4",
    "openai/api/gpt-4-0314",
    "openai/api/gpt-4-0613",
    "openai/api/gpt-4-32k",
    "openai/api/gpt-4-32k-0314",
    "openai/api/gpt-4-32k-0613",
    "openai/api/gpt-3.5-turbo",
    "openai/api/gpt-3.5-turbo-16k",
    "openai/api/gpt-3.5-turbo-0301",
    "openai/api/gpt-3.5-turbo-0613",
    "openai/api/gpt-3.5-turbo-1106",
    "openai/api/gpt-3.5-turbo-0125",
    "openai/api/gpt-3.5-turbo-16k-0613",
]

GroqModelType: TypeAlias = Literal[
    "groq/api/gemma2-9b-it",
    "groq/api/llama3-groq-70b-8192-tool-use-preview",
    "groq/api/llama3-groq-8b-8192-tool-use-preview",
    "groq/api/llama-3.1-70b-specdec",
    "groq/api/llama-3.2-1b-preview",
    "groq/api/llama-3.2-3b-preview",
    "groq/api/llama-3.2-11b-vision-preview",
    "groq/api/llama-3.2-90b-vision-preview",
    "groq/api/llama-3.3-70b-specdec",
    "groq/api/llama-3.3-70b-versatile",
    "groq/api/llama-3.1-8b-instant",
    "groq/api/llama-guard-3-8b",
    "groq/api/llama3-70b-8192",
    "groq/api/llama3-8b-8192",
    "groq/api/mixtral-8x7b-32768",
]

CerebrasModelType: TypeAlias = Literal[
    "cerebras/api/llama3.1-8b",
    "cerebras/api/llama3.1-70b",
    "cerebras/api/llama-3.3-70b",
]

DeepInfraModelType: TypeAlias = Literal[
    "deepinfra/api/meta-llama/Llama-3.3-70B-Instruct",
    "deepinfra/api/meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "deepinfra/api/meta-llama/Meta-Llama-3.1-70B-Instruct",
    "deepinfra/api/meta-llama/Meta-Llama-3.1-8B-Instruct",
    "deepinfra/api/meta-llama/Meta-Llama-3.1-405B-Instruct",
    "deepinfra/api/Qwen/QwQ-32B-Preview",
    "deepinfra/api/meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    "deepinfra/api/meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
    "deepinfra/api/Qwen/Qwen2.5-Coder-32B-Instruct",
    "deepinfra/api/nvidia/Llama-3.1-Nemotron-70B-Instruct",
    "deepinfra/api/Qwen/Qwen2.5-72B-Instruct",
    "deepinfra/api/meta-llama/Llama-3.2-90B-Vision-Instruct",
    "deepinfra/api/meta-llama/Llama-3.2-11B-Vision-Instruct",
    "deepinfra/api/microsoft/WizardLM-2-8x22B",
    "deepinfra/api/01-ai/Yi-34B-Chat",
    "deepinfra/api/Austism/chronos-hermes-13b-v2",
    "deepinfra/api/Gryphe/MythoMax-L2-13b",
    "deepinfra/api/Gryphe/MythoMax-L2-13b-turbo",
    "deepinfra/api/HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1",
    "deepinfra/api/NousResearch/Hermes-3-Llama-3.1-405B",
    "deepinfra/api/Phind/Phind-CodeLlama-34B-v2",
    "deepinfra/api/Qwen/QVQ-72B-Preview",
    "deepinfra/api/Qwen/Qwen2-72B-Instruct",
    "deepinfra/api/Qwen/Qwen2-7B-Instruct",
    "deepinfra/api/Qwen/Qwen2.5-7B-Instruct",
    "deepinfra/api/Qwen/Qwen2.5-Coder-7B",
    "deepinfra/api/Sao10K/L3-70B-Euryale-v2.1",
    "deepinfra/api/Sao10K/L3-8B-Lunaris-v1",
    "deepinfra/api/Sao10K/L3.1-70B-Euryale-v2.2",
    "deepinfra/api/bigcode/starcoder2-15b",
    "deepinfra/api/bigcode/starcoder2-15b-instruct-v0.1",
    "deepinfra/api/codellama/CodeLlama-34b-Instruct-hf",
    "deepinfra/api/codellama/CodeLlama-70b-Instruct-hf",
    "deepinfra/api/cognitivecomputations/dolphin-2.6-mixtral-8x7b",
    "deepinfra/api/cognitivecomputations/dolphin-2.9.1-llama-3-70b",
    "deepinfra/api/databricks/dbrx-instruct",
    "deepinfra/api/airoboros-70b",
    "deepinfra/api/google/codegemma-7b-it",
    "deepinfra/api/google/gemma-1.1-7b-it",
    "deepinfra/api/google/gemma-2-27b-it",
    "deepinfra/api/google/gemma-2-9b-it",
    "deepinfra/api/lizpreciatior/lzlv_70b_fp16_hf",
    "deepinfra/api/mattshumer/Reflection-Llama-3.1-70B",
    "deepinfra/api/meta-llama/Llama-2-13b-chat-hf",
    "deepinfra/api/meta-llama/Llama-2-70b-chat-hf",
    "deepinfra/api/meta-llama/Llama-2-7b-chat-hf",
    "deepinfra/api/meta-llama/Llama-3.2-1B-Instruct",
    "deepinfra/api/meta-llama/Llama-3.2-3B-Instruct",
    "deepinfra/api/meta-llama/Meta-Llama-3-70B-Instruct",
    "deepinfra/api/meta-llama/Meta-Llama-3-8B-Instruct",
    "deepinfra/api/microsoft/Phi-3-medium-4k-instruct",
    "deepinfra/api/microsoft/WizardLM-2-7B",
    "deepinfra/api/mistralai/Mistral-7B-Instruct-v0.1",
    "deepinfra/api/mistralai/Mistral-7B-Instruct-v0.2",
    "deepinfra/api/mistralai/Mistral-7B-Instruct-v0.3",
    "deepinfra/api/mistralai/Mistral-Nemo-Instruct-2407",
    "deepinfra/api/mistralai/Mixtral-8x22B-Instruct-v0.1",
    "deepinfra/api/mistralai/Mixtral-8x22B-v0.1",
    "deepinfra/api/mistralai/Mixtral-8x7B-Instruct-v0.1",
    "deepinfra/api/nvidia/Nemotron-4-340B-Instruct",
    "deepinfra/api/openbmb/MiniCPM-Llama3-V-2_5",
    "deepinfra/api/openchat/openchat-3.6-8b",
    "deepinfra/api/openchat/openchat_3.5",
]

AIModel: TypeAlias = Literal[
    # -- Google --
    GoogleModelType,
    # -- Cerebras --
    CerebrasModelType,
    # -- OpenAI --
    OpenAIModelType,
    # -- Groq --
    GroqModelType,
    # -- DeepInfra --
    DeepInfraModelType,
]

GroqTranscriptionModelType: TypeAlias = Literal[
    "groq/api/whisper-large-v3-turbo",
    "groq/api/distil-whisper-large-v3-en",
    "groq/api/whisper-large-v3",
]

OpenAITranscriptionsModelType: TypeAlias = Literal["openai/api/whisper-1"]

TranscriptionModelType: TypeAlias = Literal[
    GroqTranscriptionModelType, OpenAITranscriptionsModelType
]
