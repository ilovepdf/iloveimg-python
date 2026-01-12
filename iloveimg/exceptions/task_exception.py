"""Exception classes for the iLoveIMG Python API."""

from .base_custom_exception import BaseCustomException


class TaskException(BaseCustomException):
    """
    Exception raised for errors related to tasks in the iLoveIMG Python API.
    """
