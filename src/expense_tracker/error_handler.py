import logging
import sys


from .exceptions import ExpenseTrackerError

from typing import Callable

logger = logging.getLogger(__name__)


def handle_error(error: BaseException) -> None:
    if isinstance(error, ExpenseTrackerError):
        logger.error(f"Error: {error}")
        return
    logger.exception("An unexpected error occurred")
    if __debug__:
        raise error
    else:
        sys.exit(1)


def run_and_handle_error(func: Callable) -> None:
    try:
        func()
    except KeyboardInterrupt:
        print("\nExiting...")
    except ExpenseTrackerError as e:
        handle_error(e)
    except Exception as e:
        handle_error(e)
