from logging import Formatter, LogRecord
from typing import override
from dataclasses import dataclass

from .lib.schemas import LogSchema


@dataclass(slots=True)
class StandardFormatter(Formatter):
    @override
    def format(self, record: LogRecord) -> str:
        log = LogSchema.from_record(record, formatter=self)
        return f"{log.serialize_timestamp(log.timestamp)} [{log.level}]:\t{log.message}"
