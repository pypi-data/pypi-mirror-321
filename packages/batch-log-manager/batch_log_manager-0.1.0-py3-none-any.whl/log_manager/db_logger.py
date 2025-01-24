from functools import wraps
import traceback

from log_manager.typeclass.logging_operations import LoggingOperations


def db_logger(action_name: str, logger: LoggingOperations):
    """
    A decorator for logging database operations using a LoggingOperations implementation.
    :param action_name: The name of the action being logged.
    :param logger: An instance of LoggingOperations for handling logging.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                # Pre-action logging
                logger.log_pre_action(action_name, **kwargs)

                # Execute the wrapped function
                result = await func(*args, **kwargs)

                # Post-action success logging
                logger.log_post_action_success(action_name, **kwargs)

                return result

            except Exception as e:
                # Capture traceback and log post-action failure
                # tb_message = "".join(traceback.format_exception(None, e, e.__traceback__))
                logger.log_post_action_failure(action_name, exception=e, **kwargs)
                raise
        return wrapper
    return decorator

