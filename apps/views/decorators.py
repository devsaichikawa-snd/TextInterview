import logging
from functools import wraps
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def log_decorator(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        logger.info(
            f"Accessing view: {func.__name__} with method {request.method}\
              and path {request.path}"
        )
        try:
            response = func(request, *args, **kwargs)
            if isinstance(response, HttpResponse):
                logger.info(
                    f"View {func.__name__} executed successfully with status\
                      code {response.status_code}"
                )
            else:
                logger.warning(
                    f"View {func.__name__} did not return HttpResponse."
                )
            return response
        except Exception as e:
            logger.error(f"Error in view {func.__name__}: {e}", exc_info=True)
            raise

    return wrapper
