from logging import Formatter, LogRecord
from typing import override
from dataclasses import dataclass
from json import dumps

from .lib.schemas import LogSchema


@dataclass(slots=True)
class JSONFormatter(Formatter):
    @override
    def format(self, record: LogRecord) -> str:
        return dumps(
            LogSchema.from_record(record, formatter=self)
            .model_dump(mode="json", exclude_none=True)
        )
