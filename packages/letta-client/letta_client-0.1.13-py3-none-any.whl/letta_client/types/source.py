# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .embedding_config import EmbeddingConfig
import typing_extensions
from ..core.serialization import FieldMetadata
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Source(UncheckedBaseModel):
    """
    Representation of a source, which is a collection of files and passages.

    Parameters:
        id (str): The ID of the source
        name (str): The name of the source.
        embedding_config (EmbeddingConfig): The embedding configuration used by the source.
        user_id (str): The ID of the user that created the source.
        metadata_ (dict): Metadata associated with the source.
        description (str): The description of the source.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human-friendly ID of the Source
    """

    name: str = pydantic.Field()
    """
    The name of the source.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the source.
    """

    embedding_config: EmbeddingConfig = pydantic.Field()
    """
    The embedding configuration used by the source.
    """

    metadata: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="metadata_")
    ] = pydantic.Field(default=None)
    """
    Metadata associated with the source.
    """

    created_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this Tool.
    """

    last_updated_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this Tool.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the source was created.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the source was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
