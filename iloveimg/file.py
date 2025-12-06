"""Module for managing files with the iLoveIMG API."""

import tempfile

from .abstract_task_element import AbstractTaskElement


# pylint: disable=too-few-public-methods
class File(AbstractTaskElement):
    """Represents a file uploaded to or managed by the iLoveIMG API."""

    _DEFAULT_PAYLOAD = {"server_filename": None, "filename": None}

    def __init__(self, server_filename: str, filename: str):
        super().__init__()
        self.server_filename = server_filename
        self.filename = filename

    def _to_payload(self) -> dict:
        payload = super()._to_payload()
        payload["server_filename"] = self.server_filename
        payload["filename"] = self.filename
        return payload

    @staticmethod
    def get_temp_filename(extension=""):
        """Returns a temporary filename with the given extension."""
        with tempfile.NamedTemporaryFile(suffix=extension) as temp_file:
            return temp_file.name
