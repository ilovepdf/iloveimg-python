"""Exception class for file download errors in the iLoveIMG API."""

from .base_custom_exception import BaseCustomException


class DownloadException(BaseCustomException):
    """
    Exception raised for errors during file download in iLoveIMG API.
    """
