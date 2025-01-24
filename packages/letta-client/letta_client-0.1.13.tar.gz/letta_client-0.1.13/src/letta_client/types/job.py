# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
import datetime as dt
from .job_status import JobStatus
import typing_extensions
from ..core.serialization import FieldMetadata
from .job_type import JobType
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Job(UncheckedBaseModel):
    """
    Representation of offline jobs, used for tracking status of data loading tasks (involving parsing and embedding files).

    Parameters:
        id (str): The unique identifier of the job.
        status (JobStatus): The status of the job.
        created_at (datetime): The unix timestamp of when the job was created.
        completed_at (datetime): The unix timestamp of when the job was completed.
        user_id (str): The unique identifier of the user associated with the.
    """

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

    status: typing.Optional[JobStatus] = pydantic.Field(default=None)
    """
    The status of the job.
    """

    completed_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The unix timestamp of when the job was completed.
    """

    metadata: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="metadata_")
    ] = pydantic.Field(default=None)
    """
    The metadata of the job.
    """

    job_type: typing.Optional[JobType] = pydantic.Field(default=None)
    """
    The type of the job.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human-friendly ID of the Job
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
