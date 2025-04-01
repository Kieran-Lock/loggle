from ..lib.schemas import FilterSchema
from ..lib import FilterFactory
from ..error_filter import ErrorFilter


class Filters:
    ERROR = FilterSchema(filter_factory=FilterFactory(lambda: ErrorFilter()))
