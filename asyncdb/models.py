# Models
import uuid

from pydantic import UUID4
from sqlmodel import SQLModel, Field


class BaseModel(SQLModel, table=False):
    id: UUID4 = Field(
        primary_key=True,
        default_factory=uuid.uuid4,
        nullable=False,
        index=True,
        sa_column_kwargs={"unique": True},
    )

# class Table(BaseModel, table=True):
#     processed: bool = Field(default=False, nullable=False)
