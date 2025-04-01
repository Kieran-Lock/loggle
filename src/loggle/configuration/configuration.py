from __future__ import annotations

from typing import Literal, Self, Any
from logging.config import dictConfig as dict_config
from pydantic import BaseModel

from ..filter import FilterName, FilterSchema
from ..formatter import FormatterSchema, FormatterName
from ..handler import HandlersDict, AtomicHandlerSchema, CompositeHandlerSchema, AtomicHandlerName, CompositeHandlerName
from ..logger import LoggerName, LoggerSchema, LoggersSchema


class Configuration[T_FilterName: FilterName, T_FormatterName: FormatterName, T_HandlerName: AtomicHandlerName | CompositeHandlerName, T_LoggerName: LoggerName](BaseModel):
    version: Literal[1]
    disable_existing_loggers: bool
    filters: dict[T_FilterName, FilterSchema]
    formatters: dict[T_FormatterName, FormatterSchema]
    handlers: HandlersDict[T_HandlerName, AtomicHandlerSchema, CompositeHandlerSchema]
    loggers: dict[T_LoggerName, LoggerSchema[T_HandlerName]]

    def set_configuration(self) -> None:
        dict_config(self.to_configuration_dictionary())
    
    def to_configuration_dictionary(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True, by_alias=True)

    @classmethod
    def create(
        cls,
        *,
        filters: dict[T_FilterName, FilterSchema],
        formatters: dict[T_FormatterName, FormatterSchema],
        handlers: HandlersDict[T_HandlerName, AtomicHandlerSchema, CompositeHandlerSchema],
        loggers: LoggersSchema[T_LoggerName, T_HandlerName] | dict[T_LoggerName, LoggerSchema[T_HandlerName]],
    ) -> Self:
        return cls(
            version=1,
            disable_existing_loggers=True,
            filters=filters,
            formatters=formatters,
            handlers=handlers,
            loggers=loggers.to_loggers_dictionary() if isinstance(loggers, LoggersSchema) else loggers,
        )
