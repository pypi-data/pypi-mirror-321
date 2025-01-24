# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .letta_schemas_openai_chat_completion_request_tool_call_function import (
    LettaSchemasOpenaiChatCompletionRequestToolCallFunction,
)
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class LettaSchemasOpenaiChatCompletionRequestToolCall(UncheckedBaseModel):
    id: str
    type: typing.Optional[typing.Literal["function"]] = None
    function: LettaSchemasOpenaiChatCompletionRequestToolCallFunction

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
