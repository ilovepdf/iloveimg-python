"""Exception class for task-related errors in the iLoveIMG API."""

from .base_custom_exception import BaseCustomException


class TaskException(BaseCustomException):
    """
    Exception raised for errors related to tasks in the iLoveIMG Python API.
    """
