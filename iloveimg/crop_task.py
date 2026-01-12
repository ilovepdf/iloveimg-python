"""Handles image cropping tasks using the iLoveIMG API.

This module provides the CropTask class to configure and execute cropping of image
files.
"""

from .abstract_task_element import Payload
from .task import Task
from .validators import IntValidator


class CropTask(Task):
    """
    Handles image cropping tasks using the iLoveIMG API.

    Args:
        public_key (str, optional): API public key.
            If not provided, taken from ILOVEIMG_PUBLIC_KEY env variable.
        secret_key (str, optional): API secret key.
            If not provided, taken from ILOVEIMG_SECRET_KEY env variable.
        make_start (bool, optional): Whether to start the task immediately.
            Default is False.

    Example:
        task = CropTask(public_key="your_public_key", secret_key="your_secret_key")
    """

    _tool = "cropimage"

    _DEFAULT_PAYLOAD = {
        "width": None,
        "height": None,
        "x": 0,
        "y": 0,
    }

    @property
    def width(self) -> int:
        """
        Returns the width in pixels of the crop area.

        Returns:
            int: The width in pixels of the crop area. Must be set before execution.

        Raises:
            KeyError: If the 'width' parameter is not set.
        """
        return self._get_attr("width")

    @width.setter
    def width(self, value: int):
        """
        Sets the width in pixels of the crop area.

        Args:
            value (int): The width in pixels. Must be a positive integer.

        Raises:
            ValueError: If the provided value is not a positive integer.
        """
        IntValidator.validate_positive(value, "width")
        self._set_attr("width", value)

    @property
    def height(self) -> int:
        """
        Returns the height in pixels of the crop area.

        Returns:
            int: The height in pixels of the crop area. Must be set before execution.

        Raises:
            KeyError: If the 'height' parameter is not set.
        """
        return self._get_attr("height")

    @height.setter
    def height(self, value: int):
        """
        Sets the height in pixels of the crop area.

        Args:
            value (int): The height in pixels. Must be a positive integer.

        Raises:
            ValueError: If the provided value is not a positive integer.
        """
        IntValidator.validate_positive(value, "height")
        self._set_attr("height", value)

    @property
    def x(self) -> int:  # pylint: disable=invalid-name
        """
        Returns the horizontal starting point in pixels for cropping.

        Returns:
            int: The horizontal starting point in pixels. Default is 0.
        """
        return self._get_attr("x")

    @x.setter
    def x(self, value: int):  # pylint: disable=invalid-name
        """
        Sets the horizontal starting point in pixels for cropping.

        Args:
            value (int): The horizontal starting point in pixels.
                Must be a non-negative integer.

        Raises:
            ValueError: If the provided value is not a non-negative integer.
        """
        IntValidator.validate_positive(value, "x")
        self._set_attr("x", value)

    @property
    def y(self) -> int:  # pylint: disable=invalid-name
        """
        Returns the vertical starting point in pixels for cropping.

        Returns:
            int: The vertical starting point in pixels. Default is 0.
        """
        return self._get_attr("y")

    @y.setter
    def y(self, value: int):  # pylint: disable=invalid-name
        """
        Sets the vertical starting point in pixels for cropping.

        Args:
            value (int): The vertical starting point in pixels.
                Must be a non-negative integer.

        Raises:
            ValueError: If the provided value is not a non-negative integer.
        """
        IntValidator.validate_positive(value, "y")
        self._set_attr("y", value)

    def _validate_payload(self, payload: Payload) -> None:
        """
        Validates the payload for the crop task.

        Args:
            payload (Payload): The payload to validate.

        Raises:
            ValueError: If width or height is not specified.
        """
        super()._validate_payload(payload)
        if self.width is None:
            raise ValueError("Width must be specified.")

        if self.height is None:
            raise ValueError("Height must be specified.")

    def append_file(self, file: str):
        """
        Appends a file to the crop task.

        Args:
            file (str): The file to be added.

        Raises:
            ValueError: If a file is already added to the task.
        """
        if len(self.files) >= 1:
            raise ValueError("CropTask only supports a single file.")
        return super().append_file(file)
