from enum import StrEnum


class BaseFormatterName(StrEnum):
    pass


class FormatterName(BaseFormatterName):
    STANDARD = "standard"
    JSON = "json"
