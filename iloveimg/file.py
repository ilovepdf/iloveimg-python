"""Module for managing files with the iLoveIMG API."""

import tempfile

from .abstract_task_element import AbstractTaskElement
from .validators import StringValidator


class BaseFile(AbstractTaskElement):
    """Base class representing a base file managed by the iLovePDF API."""

    _DEFAULT_PAYLOAD = {
        "server_filename": None,
        "filename": None,
    }

    REQUIRED_FIELDS = ["server_filename", "filename"]

    def __init__(self, server_filename: str, filename: str):
        super().__init__()
        self.server_filename = server_filename
        self.filename = filename

    # Getters and Setters of filename
    @property
    def filename(self) -> str:
        """
        Gets the filename associated with the file.

        Returns:
            str: The filename. Default is None.
        """
        return self._get_attr("filename")

    @filename.setter
    def filename(self, value: str):
        """
        Sets the filename for the file.

        Args:
            value (str): The filename to associate.

        Raises:
            ValueError: If the filename is not a valid string.
        """
        StringValidator.validate(value, "filename")
        self._set_attr("filename", value)

    # Getters and Setters of server_filename
    @property
    def server_filename(self) -> str:
        """
        Gets the server filename associated with the file.

        Returns:
            str: The server filename. Default is None.
        """
        return self._get_attr("server_filename")

    @server_filename.setter
    def server_filename(self, value: str):
        """
        Sets the server filename for the file.

        Args:
            value (str): The server filename to associate.

        Raises:
            ValueError: If the server filename is not a valid string.
        """
        StringValidator.validate(value, "server_filename")
        self._set_attr("server_filename", value)

    @staticmethod
    def get_temp_filename(extension: str = "") -> str:
        """
        Returns a temporary filename with the given extension.

        Args:
            extension (str): The file extension to use.

        Returns:
            str: The path to the temporary file.
        """
        with tempfile.NamedTemporaryFile(suffix=extension) as temp_file:
            return temp_file.name


class File(BaseFile):
    """Represents a file uploaded to or managed by the iLoveIMG API."""
