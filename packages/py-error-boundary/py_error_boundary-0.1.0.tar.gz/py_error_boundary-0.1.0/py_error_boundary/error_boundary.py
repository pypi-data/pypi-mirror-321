import os 
import inspect
from logging import getLogger

Logger = getLogger()

## Colors For Error
RED = "\033[31m{error}\033[0m"
BOLD_RED = "\033[31;1m{error}\033[0m"

class ErrorBoundary:
    def __init__(self, error_handler=None):
        self.error_handler = error_handler or self.default_error_handler

    def default_error_handler(self, exception, filename, line_num):
        error_message = f"An exception occurred at line {line_num} in file {filename}. \nError: {exception}"
        Logger.error(msg=BOLD_RED.format(error=error_message))

    def __call__(self, func, *args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            inspect_stacks = inspect.stack()
            filename = os.path.basename(inspect_stacks[1].filename)
            line_num = inspect_stacks[1].lineno
            self.error_handler(e, filename, line_num)
            return None
