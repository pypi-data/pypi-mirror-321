# This file was auto-generated by Fern from our API Definition.

import typing
from .letta_schemas_letta_message_tool_call import LettaSchemasLettaMessageToolCall
from .tool_call_delta import ToolCallDelta

ToolCallMessageToolCall = typing.Union[LettaSchemasLettaMessageToolCall, ToolCallDelta]
