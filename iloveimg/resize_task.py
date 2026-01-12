"""Resize image task implementation for the iLoveIMG API.

Provides the ResizeTask class which allows resizing images either by explicit
pixel dimensions or by a percentage of their original size. Supports additional
options to maintain aspect ratio and prevent enlarging images that are smaller
than the target dimensions.

The class exposes validated properties that populate an internal payload later
sent to the iLoveIMG API when executing the task.
"""

from typing import Literal

from iloveimg.abstract_task_element import Payload

from .task import Task
from .validators import ChoiceValidator, IntValidator

RESIZE_MODE_OPTIONS = {"pixels", "percentage"}
ResizeModeType = Literal["pixels", "percentage"]


class ResizeTask(Task):
    """
    Handles image resize tasks using the iLoveIMG API.

    Args:
        public_key (str, optional): API public key. If not provided, it is
            taken from the ILOVEIMG_PUBLIC_KEY environment variable.
        secret_key (str, optional): API secret key. If not provided, it is
            taken from the ILOVEIMG_SECRET_KEY environment variable.
        make_start (bool, optional): Whether to start (initialize) the task
            immediately after construction.

    Example:
        task = ResizeTask(public_key="your_public_key", secret_key="your_secret_key")
        task.resize_mode = "pixels"
        task.pixels_width = 800
        task.pixels_height = 600
        task.maintain_ratio = True
        task.append_file("image.jpg")
    """

    _tool = "resizeimage"

    _DEFAULT_PAYLOAD = {
        "resize_mode": "pixels",
        "pixels_width": None,
        "pixels_height": None,
        "percentage": None,
        "maintain_ratio": True,
        "no_enlarge_if_smaller": True,
    }

    @property
    def resize_mode(self) -> str:
        """
        Returns the current resize mode used for resizing images.

        Returns:
            str: The current resize mode. Default is "pixels". Possible values
                are "pixels" and "percentage".
        """
        return self._get_attr("resize_mode")

    @resize_mode.setter
    def resize_mode(self, value: ResizeModeType):
        """
        Sets the resize mode.

        Args:
            value (str): Must be one of "pixels" or "percentage".

        Raises:
            InvalidChoiceError: If value is not one of the allowed resize modes.
        """
        ChoiceValidator.validate(value, RESIZE_MODE_OPTIONS, "resize_mode")
        self._set_attr("resize_mode", value)

    @property
    def pixels_width(self) -> int:
        """
        Returns the target width in pixels when using pixel-based resizing.

        Returns:
            int: The width in pixels. Required when resize_mode is "pixels".
        """
        return self._get_attr("pixels_width")

    @pixels_width.setter
    def pixels_width(self, value: int):
        """
        Sets the target width in pixels.

        Args:
            value (int): Positive integer representing the desired width.

        Raises:
            IntOutOfRangeError: If value is not a positive integer.
        """
        IntValidator.validate_positive(value, "pixels_width")
        self._set_attr("pixels_width", value)

    @property
    def pixels_height(self) -> int:
        """
        Returns the target height in pixels when using pixel-based resizing.

        Returns:
            int: The height in pixels. Required when resize_mode is "pixels".
        """
        return self._get_attr("pixels_height")

    @pixels_height.setter
    def pixels_height(self, value: int):
        """
        Sets the target height in pixels.

        Args:
            value (int): Positive integer representing the desired height.

        Raises:
            IntOutOfRangeError: If value is not a positive integer.
        """
        IntValidator.validate_positive(value, "pixels_height")
        self._set_attr("pixels_height", value)

    @property
    def percentage(self) -> int:
        """
        Returns the percentage value used for percentage-based resizing.

        Returns:
            int: The percentage value. Required when resize_mode is "percentage".
        """
        return self._get_attr("percentage")

    @percentage.setter
    def percentage(self, value: int):
        """
        Sets the percentage for resizing.

        Args:
            value (int): Positive integer indicating the scale relative to the
                original size.

        Raises:
            IntOutOfRangeError: If value is not a positive integer.
        """
        IntValidator.validate_positive(value, "percentage")
        self._set_attr("percentage", value)

    @property
    def maintain_ratio(self) -> bool:
        """
        Returns whether the aspect ratio is maintained during resizing.

        Returns:
            bool: True if the aspect ratio should be preserved. Default is True.
        """
        return self._get_attr("maintain_ratio")

    @maintain_ratio.setter
    def maintain_ratio(self, value: bool):
        """
        Sets whether to maintain the image's aspect ratio.

        Args:
            value (bool): True to preserve aspect ratio.
        """
        self._set_attr("maintain_ratio", value)

    @property
    def no_enlarge_if_smaller(self) -> bool:
        """
        Returns whether small images should be prevented from enlarging.

        Returns:
            bool: True if images smaller than target size should not be enlarged.
                Default is True.
        """
        return self._get_attr("no_enlarge_if_smaller")

    @no_enlarge_if_smaller.setter
    def no_enlarge_if_smaller(self, value: bool):
        """
        Sets whether to avoid enlarging images smaller than target dimensions.

        Args:
            value (bool): True to prevent enlargement of smaller images.
        """
        self._set_attr("no_enlarge_if_smaller", value)

    def _validate_payload(self, payload: Payload) -> None:
        """
        Validates the payload before task execution.

        Ensures required fields are present according to the resize mode.

        Args:
            payload (dict): The current payload dictionary.

        Raises:
            ValueError: If required fields are missing for the selected resize mode.
        """
        super()._validate_payload(payload)

        if self.resize_mode == "pixels":
            if (
                payload.get("pixels_width") is None
                or payload.get("pixels_height") is None
            ):
                raise ValueError("pixels_width and pixels_height are required.")
        if self.resize_mode == "percentage":
            if payload.get("percentage") is None:
                raise ValueError("percentage is required.")

    def _to_payload(self) -> Payload:
        """
        Builds the final payload to be sent to the API.

        Removes attributes that are not relevant to the selected resize mode.

        Returns:
            dict: Sanitized payload ready for API submission.
        """
        props = super()._to_payload()
        if props.get("resize_mode") != "pixels":
            props.pop("pixels_width", None)
            props.pop("pixels_height", None)
        if props.get("resize_mode") != "percentage":
            props.pop("percentage", None)
        return props
