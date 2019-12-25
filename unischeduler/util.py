from traceback import format_exception
from typing import Callable, Any


TIMEZONE = "America/New_York"
OutputHandler = Callable[[str], Any]


class SchedulerError(Exception):
    """ Common base class for all non-halting exceptions """
    pass


class ErrorHandler:
    def __init__(self, output_handler: OutputHandler, unknown_error_handler: OutputHandler = print):
        self.output_handler = output_handler
        self.unknown_error_handler = unknown_error_handler

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        if traceback is None:
            self.output_handler("Finished successfully!")
        else:
            if isinstance(value, SchedulerError):
                self.output_handler(str(value))
            else:
                self.unknown_error_handler(''.join(format_exception(type, value, traceback)))
        return True  # Suppresses exceptions for some magical reason
