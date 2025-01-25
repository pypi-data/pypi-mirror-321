from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

from workflowai.core.domain.version_reference import VersionReference

TaskInput = TypeVar("TaskInput", bound=BaseModel)
TaskOutput = TypeVar("TaskOutput", bound=BaseModel)


class Task(BaseModel, Generic[TaskInput, TaskOutput]):
    """
    A blueprint for a task. Used to instantiate task runs.

    It should not be used as is but subclassed to provide the necessary information for the task.
    Default values are provided so that they can be overriden in subclasses
    """

    id: str = ""
    schema_id: int = 0

    version: Optional[VersionReference] = None

    input_class: type[TaskInput] = BaseModel  # pyright: ignore [reportAssignmentType]
    output_class: type[TaskOutput] = BaseModel  # pyright: ignore [reportAssignmentType]
