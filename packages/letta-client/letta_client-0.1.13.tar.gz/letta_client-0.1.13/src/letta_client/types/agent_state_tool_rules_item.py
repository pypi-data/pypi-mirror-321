# This file was auto-generated by Fern from our API Definition.

import typing
from .child_tool_rule import ChildToolRule
from .init_tool_rule import InitToolRule
from .terminal_tool_rule import TerminalToolRule
from .conditional_tool_rule import ConditionalToolRule

AgentStateToolRulesItem = typing.Union[ChildToolRule, InitToolRule, TerminalToolRule, ConditionalToolRule]
