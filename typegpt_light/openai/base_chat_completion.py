from openai.types.chat import ChatCompletionContentPartParam, ChatCompletionMessageParam, ChatCompletionUserMessageParam

from typegpt_light.exceptions import LLMException
from typegpt_light.prompt_definition.image import ImagePrompt, ImageURLPrompt
from typegpt_light.prompt_definition.prompt_template import UserPrompt

from .views import OpenAIChatModel


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

    # - User Prompt Image Handling

    def _generate_user_message(self, user_prompt: UserPrompt) -> ChatCompletionUserMessageParam:
        if ImagePrompt is not None and isinstance(user_prompt, ImagePrompt):
            user_prompt = [user_prompt]
        elif isinstance(user_prompt, ImageURLPrompt):
            user_prompt = [user_prompt]

        if isinstance(user_prompt, str):
            return {"role": "user", "content": user_prompt}
        else:
            content_parts: list[ChatCompletionContentPartParam] = []
            for content in user_prompt:
                if isinstance(content, str):
                    content_parts.append({"type": "text", "text": content})
                elif ImagePrompt is not None and isinstance(content, ImagePrompt):
                    content_parts.append(
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{content._encode_image(content.image)}",
                                "detail": content.quality,
                            },
                        }
                    )
                elif isinstance(content, ImageURLPrompt):
                    content_parts.append({"type": "image_url", "image_url": {"url": content.image_url, "detail": content.quality}})

            return {"role": "user", "content": content_parts}

    # - Exception Handling

    # def _inject_exception_details(self, e: LLMException, messages: list[ChatCompletionMessageParam], raw_completion: str):
    #     system_prompt = next((m["content"] for m in messages if m["role"] == "system"), None)
    #     user_prompt = next((m["content"] for m in messages if m["role"] == "user"), None)

    #     e.system_prompt = system_prompt
    #     e.user_prompt = user_prompt
    #     e.raw_completion = raw_completion
