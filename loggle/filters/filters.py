from .lib.consts import FilterName
from .lib.schemas import FilterSchema
from .lib import FilterFactory
from .error_filter import ErrorFilter


LOGGLE_FILTERS = {
    FilterName.ERROR: FilterSchema(
        filter_factory=FilterFactory(lambda: ErrorFilter()),
    ),
}
