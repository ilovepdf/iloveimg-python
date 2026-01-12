"""Exception package for iLoveIMG Python library.

This package contains custom exception classes used throughout the
iLoveIMG API integration.
"""

from .auth_exception import AuthException
from .base_custom_exception import BaseCustomException
from .choice_errors import (
    InvalidChoiceError,
)
from .download_exception import DownloadException
from .int_errors import (
    IntNotInAllowedSetError,
    IntOutOfRangeError,
    InvalidIntValueError,
    NegativeIntError,
    NotAnIntError,
    ZeroIntError,
)
from .not_implemented_exception import NotImplementedException
from .path_exception import PathException
from .process_exception import ProcessException
from .signature_exception import SignatureException
from .start_exception import StartException
from .task_exception import TaskException
from .upload_exception import UploadException

__all__ = [
    "AuthException",
    "DownloadException",
    "NotImplementedException",
    "PathException",
    "ProcessException",
    "SignatureException",
    "StartException",
    "TaskException",
    "UploadException",
    "NotAnIntError",
    "InvalidIntValueError",
    "IntOutOfRangeError",
    "NegativeIntError",
    "ZeroIntError",
    "IntNotInAllowedSetError",
    "InvalidChoiceError",
    "BaseCustomException",
]
