# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class AgentEnvironmentVariable(UncheckedBaseModel):
    created_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this object.
    """

    last_updated_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the object was created.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the object was last updated.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human-friendly ID of the Agent-env
    """

    key: str = pydantic.Field()
    """
    The name of the environment variable.
    """

    value: str = pydantic.Field()
    """
    The value of the environment variable.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional description of the environment variable.
    """

    agent_id: str = pydantic.Field()
    """
    The ID of the agent this environment variable belongs to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
