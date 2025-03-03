from __future__ import annotations

from logging import LogRecord, Formatter
from pathlib import Path
from datetime import datetime, timezone
from typing import Self

from pydantic import BaseModel, ConfigDict, field_serializer, Field
from pydantic.alias_generators import to_camel

from ...lib.consts import LoggingLevel
from .formatter_factory import FormatterFactory


class JSONLogModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
    )


class FormatterModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
    )


class JSONLogProcessSchema(JSONLogModel):
    name: str | None
    id: int | None


class JSONLogThreadSchema(JSONLogModel):
    name: str | None
    id: int | None


class LogSchema(JSONLogModel):
    timestamp: datetime
    level: LoggingLevel
    message: str
    file_path: Path
    line_number: int
    exception: str | None
    stack: str | None
    process: JSONLogProcessSchema
    thread: JSONLogThreadSchema
    logger: str

    @field_serializer("timestamp")
    def serialize_timestamp(self, timestamp: datetime) -> str:
        return timestamp.strftime(f"%d/%m/%Y %H:%M:%S.{timestamp.microsecond:>06}")
    
    @classmethod
    def from_record(cls, record: LogRecord, *, formatter: Formatter) -> Self:
        return cls(
            timestamp=datetime.fromtimestamp(record.created, tz=timezone.utc),
            level=record.levelname,
            message=record.getMessage(),
            file_path=record.pathname,
            line_number=record.lineno,
            exception=formatter.formatException(record.exc_info) if record.exc_info else None,
            stack=formatter.formatStack(record.stack_info) if record.exc_info else None,
            process=JSONLogProcessSchema(name=record.processName, id=record.process),
            thread=JSONLogThreadSchema(name=record.threadName, id=record.thread),
            logger=record.name,
        )


class FormatterSchema(FormatterModel):
    format: str | None = None
    datefmt: str | None = None
    formatter_factory: FormatterFactory | None = Field(alias="()", serialization_alias="()", default=None)
