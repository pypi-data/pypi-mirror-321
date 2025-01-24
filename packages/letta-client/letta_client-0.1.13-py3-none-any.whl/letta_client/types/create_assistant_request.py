# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CreateAssistantRequest(UncheckedBaseModel):
    model: str = pydantic.Field()
    """
    The model to use for the assistant.
    """

    name: str = pydantic.Field()
    """
    The name of the assistant.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the assistant.
    """

    instructions: str = pydantic.Field()
    """
    The instructions for the assistant.
    """

    tools: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The tools used by the assistant.
    """

    file_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of file IDs associated with the assistant.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Metadata associated with the assistant.
    """

    embedding_model: typing.Optional[str] = pydantic.Field(default=None)
    """
    The model to use for the assistant.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
