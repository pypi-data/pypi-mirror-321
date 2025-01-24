# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class ReasoningMessage(UncheckedBaseModel):
    """
    Representation of an agent's internal reasoning.

    Attributes:
        reasoning (str): The internal reasoning of the agent
        id (str): The ID of the message
        date (datetime): The date the message was created in ISO format
    """

    id: str
    date: dt.datetime
    reasoning: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
