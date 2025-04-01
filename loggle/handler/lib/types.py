from typing import overload, Any

from pydantic_core import CoreSchema, core_schema
from pydantic import GetCoreSchemaHandler

from .consts import AtomicHandlerName, AtomicHandlerName, CompositeHandlerName, CompositeHandlerName
from .schemas import HandlerModel, StreamHandlerSchema, FileHandlerSchema, QueueHandlerSchema
from ...formatter.lib.consts import FormatterName


type HandlerName = AtomicHandlerName | CompositeHandlerName


class HandlersDict[K: HandlerName, V_AtomicHandler: HandlerModel, V_CompositeHandler: HandlerModel](dict[K, V_AtomicHandler | V_CompositeHandler]):
    @overload
    def __getitem__(self, key: AtomicHandlerName) -> V_AtomicHandler:
        ...
    
    @overload
    def __getitem__(self, key: CompositeHandlerName) -> V_CompositeHandler:
        ...

    def __getitem__(self, key: K) -> V_AtomicHandler | V_CompositeHandler:
        return super(HandlersDict, self).__getitem__(key)
    
    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler: GetCoreSchemaHandler) -> CoreSchema:
        return core_schema.no_info_after_validator_function(cls, handler(dict))
