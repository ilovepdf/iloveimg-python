"""Exception class for errors during the start of a task in the iLoveIMG API."""

from .base_custom_exception import BaseCustomException


class StartException(BaseCustomException):
    """
    Exception raised for errors that occur during the start of a task in the iLoveIMG
        API.
    """
