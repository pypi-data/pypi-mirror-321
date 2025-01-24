# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SandboxEnvironmentVariableCreate(UncheckedBaseModel):
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
