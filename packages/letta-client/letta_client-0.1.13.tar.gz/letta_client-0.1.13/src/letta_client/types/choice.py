# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
from .letta_schemas_openai_chat_completion_response_message import LettaSchemasOpenaiChatCompletionResponseMessage
import typing
from .message_content_log_prob import MessageContentLogProb
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class Choice(UncheckedBaseModel):
    finish_reason: str
    index: int
    message: LettaSchemasOpenaiChatCompletionResponseMessage
    logprobs: typing.Optional[typing.Dict[str, typing.Optional[typing.List[MessageContentLogProb]]]] = None
    seed: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
