from typegpt_light.exceptions import LLMException


from .views import OpenAIChatModel

from openai.types.chat import ChatCompletionMessageParam


class BaseChatCompletions:
    @staticmethod
    def max_tokens_of_model(model: OpenAIChatModel) -> int:
        match model:
            case "gpt-3.5-turbo-0301" | "gpt-3.5-turbo-0613":
                return 4096
            case "gpt-3.5-turbo" | "gpt-3.5-turbo-16k" | "gpt-3.5-turbo-16k-0613" | "gpt-3.5-turbo-1106" | "gpt-3.5-turbo-0125":
                return 16384
            case "gpt-4" | "gpt-4-0314" | "gpt-4-0613":
                return 8192
            case "gpt-4-32k" | "gpt-4-32k-0314" | "gpt-4-32k-0613":
                return 32768
            case (
                "gpt-4-turbo-preview"
                | "gpt-4-1106-preview"
                | "gpt-4-0125-preview"
                | "gpt-4-vision-preview"
                | "gpt-4-turbo"
                | "gpt-4-turbo-2024-04-09"
                | "gpt-4o"
                | "gpt-4o-2024-05-13"
                | "gpt-4o-2024-08-06"
                | "gpt-4o-mini"
                | "gpt-4o-mini-2024-07-18"
            ):
                return 128_000

    # - Exception Handling

    # def _inject_exception_details(self, e: LLMException, messages: list[ChatCompletionMessageParam], raw_completion: str):
    #     system_prompt = next((m["content"] for m in messages if m["role"] == "system"), None)
    #     user_prompt = next((m["content"] for m in messages if m["role"] == "user"), None)

    #     e.system_prompt = system_prompt
    #     e.user_prompt = user_prompt
    #     e.raw_completion = raw_completion
