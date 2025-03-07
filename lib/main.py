from time import sleep

from .logger import LOGGER


def some_lib_func(n: int = 5) -> str:
    if n > 5:
        LOGGER.error("Failure", extra=n)
        return "Failure"
    for i in range(n):
        LOGGER.info(i)
        sleep(0.4)
    return "Success"
