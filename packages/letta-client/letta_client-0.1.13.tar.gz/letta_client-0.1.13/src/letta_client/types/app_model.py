# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import typing
from .app_auth_scheme import AppAuthScheme
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class AppModel(UncheckedBaseModel):
    """
    App data model.
    """

    name: str
    key: str
    app_id: typing_extensions.Annotated[str, FieldMetadata(alias="appId")]
    description: str
    categories: typing.List[str]
    meta: typing.Dict[str, typing.Optional[typing.Any]]
    logo: typing.Optional[str] = None
    docs: typing.Optional[str] = None
    group: typing.Optional[str] = None
    status: typing.Optional[str] = None
    enabled: typing.Optional[bool] = None
    no_auth: typing.Optional[bool] = None
    auth_schemes: typing.Optional[typing.List[AppAuthScheme]] = None
    test_connectors: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Optional[typing.Any]]]],
        FieldMetadata(alias="testConnectors"),
    ] = None
    documentation_doc_text: typing.Optional[str] = None
    configuration_docs_text: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
