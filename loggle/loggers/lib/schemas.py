from pydantic import ConfigDict, BaseModel
from typing import Self
from json import loads
from pathlib import Path

from ...handlers.lib.types import HandlerName
from .consts import LoggerName
from ...lib.consts import LoggingLevel


class LoggerModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
    )


class LoggerSchema(LoggerModel):
    handlers: list[HandlerName]
    level: LoggingLevel
    propagate: bool


class LoggersSchema(LoggerModel):
    loggers: dict[LoggerName, LoggerSchema]

    def to_loggers_dictionary(self) -> dict[LoggerName, LoggerSchema]:
        return {logger_name: logger_schema.model_dump(exclude_none=True) for logger_name, logger_schema in self.loggers.items()}

    @classmethod
    def from_path(cls, path: Path) -> Self:
        return cls.model_validate(loads(path.read_text()), from_attributes=False)
