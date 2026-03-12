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
from .file_errors import FileExtensionNotAllowed, FileTooLargeError
from .float_errors import (
    FloatNotInAllowedSetError,
    FloatOutOfRangeError,
    InvalidFloatValueError,
    NegativeFloatError,
    NotAFloatError,
    ZeroFloatError,
)
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
from .payload_field_errors import MissingPayloadFieldError
from .process_exception import ProcessException
from .signature_exception import SignatureException
from .start_exception import StartException
from .task_error import TaskConfigurationError
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
    "MissingPayloadFieldError",
    "FileExtensionNotAllowed",
    "FileTooLargeError",
    "FloatNotInAllowedSetError",
    "FloatOutOfRangeError",
    "InvalidFloatValueError",
    "NegativeFloatError",
    "NotAFloatError",
    "ZeroFloatError",
    "TaskConfigurationError",
]
