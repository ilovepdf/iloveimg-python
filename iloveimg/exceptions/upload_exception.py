"""Exception class for file upload errors in iLoveIMG API."""

from .base_custom_exception import BaseCustomException


class UploadException(BaseCustomException):
    """
    Exception raised for errors during file upload in iLoveIMG API.
    """
