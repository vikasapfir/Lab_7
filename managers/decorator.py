"""
Module: decorator

This module provides a decorator for logging exceptions raised by a function.
"""

import logging

def logged(exception, mode):
    """
    Decorator that logs exceptions raised by a function.

    Args:
        exception: The exception class to catch.
        mode (str): The logging mode. Valid values are 'console' or 'file'.

    Returns:
        The decorated function.

    Raises:
        ValueError: If an invalid mode value is provided.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as exception:
                if mode == 'console':
                    logging.error("Exception: %s", exception)
                elif mode == 'file':
                    logging.basicConfig(filename="log.log", level=logging.ERROR, \
format='%(asctime)s %(levelname)s %(message)s', datefmt="%Y-%m-%d %I:%M:%S%p")
                    logging.error("Exception: %s", exception)
                else:
                    raise ValueError("Invalid mode value!") from exception

        return wrapper

    return decorator
