"""Module containing custom exceptions for iLoveIMG API."""

from .base_custom_exception import BaseCustomException


class DownloadException(BaseCustomException):
    """
    Exception raised for errors during file download in iLoveIMG API.
    """
