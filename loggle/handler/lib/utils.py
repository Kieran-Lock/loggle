def import_qualified_name[T](name: str) -> T:
    parts = name.split(".")
    module = parts.pop(0)
    found = __import__(module)
    for part in parts:
        module = f"{module}.{part}"
        try:
            found = getattr(found, part)
        except AttributeError:
            __import__(module)
            found = getattr(found, part)
    return found
