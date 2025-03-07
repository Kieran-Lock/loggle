from __future__ import annotations

from typing import Literal, Self, Any
from logging.config import dictConfig as dict_config
from pydantic import BaseModel

from ..handlers import QueueHandler
from ..formatters import FormatterSchema, FormatterName, LOGGLE_FORMATTERS
from ..handlers import HandlerName, HandlerSchema, QueueHandlerName, LOGGLE_HANDLERS
from ..loggers import LoggerName, LoggerSchema, LoggersSchema


class LoggingConfiguration(BaseModel):
    version: Literal[1]
    disable_existing_loggers: bool
    formatters: dict[FormatterName, FormatterSchema]
    handlers: dict[HandlerName, HandlerSchema]
    loggers: dict[LoggerName, LoggerSchema]

    def set_configuration(self) -> None:
        dict_config(self.to_configuration_dictionary())
        if QueueHandlerName.QUEUE in self.handlers:
            QueueHandler.get().start_listener()
    
    def to_configuration_dictionary(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True, by_alias=True)

    @classmethod
    def create(
        cls,
        *,
        formatters: dict[FormatterName, FormatterSchema],
        handlers: dict[HandlerName, HandlerSchema],
        loggers: LoggersSchema | dict[LoggerName, LoggerSchema],
    ) -> Self:
        return cls(
            version=1,
            disable_existing_loggers=True,
            formatters=formatters,
            handlers=handlers,
            loggers=loggers.to_loggers_dictionary() if isinstance(loggers, LoggersSchema) else loggers,
        )
    
    @classmethod
    def default(cls, *, loggers: LoggersSchema | dict[LoggerName, LoggerSchema]) -> Self:
        return cls.create(
            formatters=LOGGLE_FORMATTERS,
            handlers=LOGGLE_HANDLERS,
            loggers=loggers,
        )
