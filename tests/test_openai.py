import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")

from typing import List, Optional, Union
from unittest.mock import Mock

import pytest
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion
from openai.types.chat.chat_completion import Choice
from openai.types.chat.chat_completion_message import ChatCompletionMessage

from typegpt_light import PromptTemplate
from typegpt_light.exceptions import LLMTokenLimitExceeded
from typegpt_light.openai import AsyncTypeAzureOpenAI, AsyncTypeOpenAI, OpenAIChatModel, TypeAzureOpenAI, TypeOpenAI


class TestOpenAIChatCompletion:

    def test_max_token_counter(self):
        # check if test covers all models (increase if new models are added)
        assert len(OpenAIChatModel.__args__) == 24  #  type: ignore

        client = AsyncTypeOpenAI(api_key="mock")

        assert client.chat.completions.max_tokens_of_model("gpt-3.5-turbo") == 16384
        assert client.chat.completions.max_tokens_of_model("gpt-3.5-turbo-0301") == 4096
        assert client.chat.completions.max_tokens_of_model("gpt-3.5-turbo-0613") == 4096
        assert client.chat.completions.max_tokens_of_model("gpt-3.5-turbo-1106") == 16384
        assert client.chat.completions.max_tokens_of_model("gpt-3.5-turbo-0125") == 16384
        assert client.chat.completions.max_tokens_of_model("gpt-3.5-turbo-16k") == 16384
        assert client.chat.completions.max_tokens_of_model("gpt-3.5-turbo-16k-0613") == 16384
        assert client.chat.completions.max_tokens_of_model("gpt-4") == 8192
        assert client.chat.completions.max_tokens_of_model("gpt-4-0314") == 8192
        assert client.chat.completions.max_tokens_of_model("gpt-4-0613") == 8192
        assert client.chat.completions.max_tokens_of_model("gpt-4-32k") == 32768
        assert client.chat.completions.max_tokens_of_model("gpt-4-32k-0314") == 32768
        assert client.chat.completions.max_tokens_of_model("gpt-4-32k-0613") == 32768
        assert client.chat.completions.max_tokens_of_model("gpt-4-turbo-preview") == 128_000
        assert client.chat.completions.max_tokens_of_model("gpt-4-1106-preview") == 128_000
        assert client.chat.completions.max_tokens_of_model("gpt-4-0125-preview") == 128_000
        assert client.chat.completions.max_tokens_of_model("gpt-4-vision-preview") == 128_000
        assert client.chat.completions.max_tokens_of_model("gpt-4-turbo") == 128_000
        assert client.chat.completions.max_tokens_of_model("gpt-4-turbo-2024-04-09") == 128_000
        assert client.chat.completions.max_tokens_of_model("gpt-4o") == 128_000
        assert client.chat.completions.max_tokens_of_model("gpt-4o-2024-05-13") == 128_000
        assert client.chat.completions.max_tokens_of_model("gpt-4o-2024-08-06") == 128_000
        assert client.chat.completions.max_tokens_of_model("gpt-4o-mini") == 128_000
        assert client.chat.completions.max_tokens_of_model("gpt-4o-mini-2024-07-18") == 128_000

    # -
