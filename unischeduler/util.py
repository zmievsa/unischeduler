from pathlib import Path
from traceback import print_exception


TIMEZONE = "America/New_York"


class SchedulerError(Exception):
    pass


class ErrorHandler:
    def __init__(self, handler_method):
        self.handler_method = handler_method
    
    def __enter__(self):
        pass
   
    def __exit__(self, type, value, traceback):
        if traceback is None:
            self.handler_method("Finished successfully!")
        else:
            log_path = Path(__file__).parent / "log.txt"
            with open(log_path, 'w') as f:
                print_exception(type, value, traceback)
                print_exception(type, value, traceback, file=f)
            if isinstance(value, SchedulerError):
                self.handler_method(str(value))
            else:
                self.handler_method('UNKNOWN ERROR OCCURRED. CHECK LOG FILE')
        return True  # Suppresses exceptions for some magical reason