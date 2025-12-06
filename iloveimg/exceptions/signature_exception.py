"""Exception class for signature processing errors in iLoveIMG API."""

from .base_custom_exception import BaseCustomException


class SignatureException(BaseCustomException):
    """
    Exception raised for errors related to signature processing in iLoveIMG API.
    """
