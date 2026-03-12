"""
Handles image conversion tasks using the iLoveIMG API.

Provides the ConvertTask class to configure and execute image conversion.
Allows conversion between formats such as JPG, PNG, GIF, GIF_ANIMATION, and HEIC.
"""

from typing import Literal

from iloveimg.exceptions import TaskConfigurationError

from .abstract_task_element import Payload
from .task import Task
from .validators import ChoiceValidator, IntValidator
from .validators.bool_validator import BoolValidator

OutputFormatType = Literal["jpg", "png", "gif", "gif_animation"]
OUTPUT_FORMAT_OPTIONS = {"jpg", "png", "gif", "gif_animation"}


class ConvertTask(Task):
    """
    Handles image conversion tasks using the iLoveIMG API.

    Args:
        public_key (str, optional): API public key.
            Uses ILOVEIMG_PUBLIC_KEY env variable if not provided.
        secret_key (str, optional): API secret key.
            Uses ILOVEIMG_SECRET_KEY env variable if not provided.
        make_start (bool, optional): Start the task immediately. Default is False.

    Example:
        task = ConvertTask(public_key="your_public_key", secret_key="your_secret_key")
    """

    _tool = "convertimage"

    _DEFAULT_PAYLOAD = {
        "convert_to": "jpg",
        "gif_time": 50,
        "gif_loop": True,
    }

    _EXTENSION_MAP = {
        "jpg": {"png", "gif", "tif", "psd", "svg", "webp", "heic", "raw"},
        "png": {"jpg"},
        "gif": {"jpg"},
        "gif_animation": {"jpg"},
    }

    def get_extension_list(self) -> list:
        """
        Gets the list of supported input extensions for conversion.

        Returns:
            list: Supported input extensions.
        """
        current_list = super().get_extension_list()
        additional_list = ["psd", "svg", "heic", "raw"]
        return current_list + additional_list

    @property
    def convert_to(self) -> OutputFormatType:
        """
        Gets the output format for image conversion.

        Returns:
            OutputFormatType: The current value. Default is "jpg".
        """
        return self._get_attr("convert_to")

    @convert_to.setter
    def convert_to(self, value: OutputFormatType):
        """
        Sets the output format.

        Args:
            value (OutputFormatType): Must be one of "jpg", "png", "gif",
                "gif_animation".

        Raises:
            InvalidChoiceError: If value is not one of the allowed output formats.
        """
        ChoiceValidator.validate(value, OUTPUT_FORMAT_OPTIONS, "convert_to")
        self._set_attr("convert_to", value)

    @property
    def gif_time(self) -> int | None:
        """
        Gets GIF animation time (hundredths of a second).

        Returns:
            int | None: The current value. Default is 50 if convert_to is
                "gif_animation", otherwise None.
        """
        if self.convert_to != "gif_animation":
            return None
        return self._get_attr("gif_time")

    @gif_time.setter
    def gif_time(self, value: int):
        """
        Sets GIF animation time (hundredths of a second).

        Args:
            value (int): Must be a positive integer.

        Raises:
            ValueError: If not positive integer or convert_to is not 'gif_animation'.
        """
        if self.convert_to != "gif_animation":
            raise TaskConfigurationError(
                "gif_time can only be set if 'convert_to' is 'gif_animation'."
            )
        IntValidator.validate_positive(value)
        self._set_attr("gif_time", value)

    @property
    def gif_loop(self) -> bool | None:
        """
        Gets GIF animation loop option.

        Returns:
            bool | None: The current value. Default is True if convert_to is
                "gif_animation", otherwise None.
        """
        if self.convert_to != "gif_animation":
            return None
        return bool(self._get_attr("gif_loop"))

    @gif_loop.setter
    def gif_loop(self, value: bool):
        """
        Sets GIF animation loop option.

        Args:
            value (bool): Must be True for loop forever, False to stop at end.

        Raises:
            ValueError: If not boolean or convert_to is not 'gif_animation'.
        """
        if self.convert_to != "gif_animation":
            raise TaskConfigurationError(
                "gif_loop can only be set if 'convert_to' is 'gif_animation'."
            )
        BoolValidator.validate(value)
        self._set_attr("gif_loop", value)

    def _to_payload(self) -> Payload:
        """
        Returns a dictionary of task parameters for API requests.

        Returns:
            Payload: Task parameters.
        """
        props = super()._to_payload()
        # Only include gif_time and gif_loop if 'convert_to' is gif_animation
        if props.get("convert_to") != "gif_animation":
            props.pop("gif_time", None)
            props.pop("gif_loop", None)
        else:
            # Ensure gif_loop is a boolean
            props["gif_loop"] = bool(props.get("gif_loop", True))
        return props

    def _validate_payload(self, payload: Payload) -> None:
        """
        Validates the payload for the conversion task.

        Args:
            payload (Payload): The payload to validate.

        Raises:
            ValueError: If file extensions are not supported for the selected output
                format.
        """
        super()._validate_payload(payload)

        if "files" in payload:
            output_format = self.convert_to
            extension_list = self._get_extension_list(output_format)
            for file in payload["files"]:
                self._validate_file_extension(file["filename"], extension_list)

    @classmethod
    def _get_extension_list(cls, output_format: str) -> list:
        """
        Gets the set of supported input extensions for the given output format.

        Args:
            output_format (str): Desired output format.

        Raises:
            ValueError: If output_format is not valid.

        Returns:
            list: Supported input extensions.
        """
        if output_format not in OUTPUT_FORMAT_OPTIONS:
            raise ValueError(f"Invalid output format: {output_format}.")
        return list(cls._EXTENSION_MAP.get(output_format, set()))
