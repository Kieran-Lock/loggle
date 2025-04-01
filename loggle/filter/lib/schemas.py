from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from .filter_factory import FilterFactory


class FilterSchema(BaseModel):
    format: str | None = None
    datefmt: str | None = None
    filter_factory: FilterFactory | None = Field(serialization_alias="()", default=None)

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
    )
