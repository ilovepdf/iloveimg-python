"""Handles watermark tasks using the iLoveIMG API.

Provides classes to configure and execute watermarking of image files.
Supports text and image watermarks with customization options.

Example:
    task = WatermarkTask(public_key="your_public_key", secret_key="your_secret_key")
    element = task.add_element()
    element.type = "text"
    element.text = "Sample Watermark"
"""

from __future__ import annotations

from typing import Literal

from .abstract_task_element import AbstractTaskElement, Payload
from .file import File
from .task import Task
from .validators import ChoiceValidator, IntValidator

WatermarkType = Literal["text", "image"]
WATERMARK_TYPE_OPTIONS = {"text", "image"}

GravityType = Literal[
    "North",
    "NorthEast",
    "NorthWest",
    "Center",
    "CenterEast",
    "CenterWest",
    "East",
    "West",
    "South",
    "SouthEast",
    "SouthWest",
]
GRAVITY_OPTIONS = {
    "North",
    "NorthEast",
    "NorthWest",
    "Center",
    "CenterEast",
    "CenterWest",
    "East",
    "West",
    "South",
    "SouthEast",
    "SouthWest",
}

FontFamilyType = Literal[
    "Arial",
    "Arial Unicode MS",
    "Verdana",
    "Courier",
    "Times New Roman",
    "Comic Sans MS",
    "WenQuanYi Zen Hei",
    "Lohit Marathi",
]
FONT_FAMILY_OPTIONS = {
    "Arial",
    "Arial Unicode MS",
    "Verdana",
    "Courier",
    "Times New Roman",
    "Comic Sans MS",
    "WenQuanYi Zen Hei",
    "Lohit Marathi",
}

FontStyleType = Literal[None, "Bold", "Italic"]
FONT_STYLE_OPTIONS = {None, "Bold", "Italic"}


class WatermarkElement(AbstractTaskElement):
    """
    Represents an element for watermark tasks.

    Allows configuration of text or image watermark properties.

    Args:
        parent_task (Optional[WatermarkTask]): The parent watermark task.

    Example:
        element = WatermarkElement(parent_task)
        element.type = "text"
        element.text = "Confidential"
    """

    _DEFAULT_PAYLOAD = {
        "type": "text",
        "text": None,
        "gravity": "Center",
        "vertical_adjustment_percent": 0,
        "horizontal_adjustment_percent": 0,
        "rotation": 0,
        "font_family": "Arial",
        "font_style": None,
        "font_size": 14,
        "font_color": "#000000",
        "transparency": 100,
        "mosaic": False,
        "x_pos_percent": 0,
        "y_pos_percent": 0,
        "width_percent": 100,
        "height_percent": 100,
        "server_filename": None,
    }

    def __init__(self, parent_task: WatermarkTask | None = None):
        super().__init__()
        self._parent_task = parent_task
        self._file: File | None = None

    @property
    def type(self) -> WatermarkType:
        """
        Gets the watermark type.

        Returns:
            WatermarkType: The current value. Default is "text".
        """
        return self._get_attr("type")

    @type.setter
    def type(self, value: WatermarkType):
        """
        Sets the watermark type.

        Args:
            value (WatermarkType): Must be one of "text" or "image".

        Raises:
            InvalidChoiceError: If value is not one of the allowed types.
        """
        ChoiceValidator.validate(value, WATERMARK_TYPE_OPTIONS, "type")
        self._set_attr("type", value)

    @property
    def text(self) -> str:
        """
        Gets the text for text watermark.

        Returns:
            str: The watermark text.

        Raises:
            TypeError: If watermark type is not "text".
        """
        if self.type != "text":
            raise TypeError("Text property is only available for text type watermark.")
        return self._get_attr("text")

    @text.setter
    def text(self, value: str):
        """
        Sets the text for text watermark.

        Args:
            value (str): The watermark text.

        Raises:
            TypeError: If watermark type is not "text" or value is not a string.
        """
        if self.type != "text":
            raise TypeError("Text property is only available for text type watermark.")
        if not isinstance(value, str):
            raise TypeError("Invalid text value: must be a string.")
        self._set_attr("text", value)

    @property
    def server_filename(self) -> str | None:
        """
        Gets the image identifier for image watermark.

        Returns:
            str | None: The image value. Default is None.

        Raises:
            TypeError: If watermark type is not "image".
        """
        if self.type != "image":
            raise TypeError(
                "server_filename property is only available for image type watermark."
            )
        return self._get_attr("server_filename")

    @property
    def gravity(self) -> GravityType:
        """
        Gets the gravity.

        Returns:
            GravityType: The current value. Default is "Center".
        """
        return self._get_attr("gravity")

    @gravity.setter
    def gravity(self, value: GravityType):
        """
        Sets the gravity.

        Args:
            value (GravityType): Must be one of the allowed gravity options.

        Raises:
            InvalidChoiceError: If value is not one of the allowed gravity options.
        """
        ChoiceValidator.validate(value, GRAVITY_OPTIONS, "gravity")
        self._set_attr("gravity", value)

    @property
    def vertical_adjustment_percent(self) -> int:
        """
        Gets the vertical adjustment percent.

        Returns:
            int: The current value. Default is 0.
        """
        return self._get_attr("vertical_adjustment_percent")

    @vertical_adjustment_percent.setter
    def vertical_adjustment_percent(self, value: int):
        """
        Sets the vertical adjustment percent.

        Args:
            value (int): Must be between -100 and 100.

        Raises:
            ValueError: If the value is out of range.
        """
        IntValidator.validate_range(value, -100, 100, "vertical adjustment percent")
        self._set_attr("vertical_adjustment_percent", value)

    @property
    def horizontal_adjustment_percent(self) -> int:
        """
        Gets the horizontal adjustment percent.

        Returns:
            int: The current value. Default is 0.
        """
        return self._get_attr("horizontal_adjustment_percent")

    @horizontal_adjustment_percent.setter
    def horizontal_adjustment_percent(self, value: int):
        """
        Sets the horizontal adjustment percent.

        Args:
            value (int): Must be between -100 and 100.

        Raises:
            ValueError: If the value is out of range.
        """
        IntValidator.validate_range(value, -100, 100, "horizontal adjustment percent")
        self._set_attr("horizontal_adjustment_percent", value)

    @property
    def rotation(self) -> int:
        """
        Gets the rotation for the watermark.

        Returns:
            int: The current value. Default is 0.
        """
        return self._get_attr("rotation")

    @rotation.setter
    def rotation(self, value: int):
        """
        Sets the rotation for the watermark.

        Args:
            value (int): Must be between 0 and 360.

        Raises:
            ValueError: If the value is out of range.
        """
        IntValidator.validate_range(value, 0, 360, "rotation")
        self._set_attr("rotation", value)

    @property
    def font_family(self) -> FontFamilyType:
        """
        Gets the font family.

        Returns:
            FontFamilyType: The current value. Default is "Arial".
        """
        return self._get_attr("font_family")

    @font_family.setter
    def font_family(self, value: FontFamilyType):
        """
        Sets the font family.

        Args:
            value (FontFamilyType): Must be one of the allowed font families.

        Raises:
            InvalidChoiceError: If value is not one of the allowed font families.
        """
        ChoiceValidator.validate(value, FONT_FAMILY_OPTIONS, "font_family")
        self._set_attr("font_family", value)

    @property
    def font_style(self) -> FontStyleType:
        """
        Gets the font style.

        Returns:
            FontStyleType: The current value. Default is None.
        """
        return self._get_attr("font_style")

    @font_style.setter
    def font_style(self, value: FontStyleType):
        """
        Sets the font style.

        Args:
            value (FontStyleType): Must be one of the allowed font styles.

        Raises:
            InvalidChoiceError: If value is not one of the allowed font styles.
        """
        ChoiceValidator.validate(value, FONT_STYLE_OPTIONS, "font_style")
        self._set_attr("font_style", value)

    @property
    def font_size(self) -> int:
        """
        Gets the font size for the watermark.

        Returns:
            int: The current value. Default is 14.
        """
        return self._get_attr("font_size")

    @font_size.setter
    def font_size(self, value: int):
        """
        Sets the font size for the watermark.

        Args:
            value (int): Must be between 0 and 1000.

        Raises:
            ValueError: If the value is out of range.
        """
        IntValidator.validate_range(value, 0, 1000, "font size")
        self._set_attr("font_size", value)

    @property
    def font_color(self) -> str:
        """
        Gets the font color for the watermark.

        Returns:
            str: The current value. Default is "#000000".
        """
        return self._get_attr("font_color")

    @font_color.setter
    def font_color(self, value: str):
        """
        Sets the font color for the watermark.

        Args:
            value (str): Must be a string.

        Raises:
            TypeError: If value is not a string.
        """
        if not isinstance(value, str):
            raise TypeError("Font color value must be a string.")
        self._set_attr("font_color", value)

    @property
    def transparency(self) -> int:
        """
        Gets the transparency for the watermark.

        Returns:
            int: The current value. Default is 100.
        """
        return self._get_attr("transparency")

    @transparency.setter
    def transparency(self, value: int):
        """
        Sets the transparency for the watermark.

        Args:
            value (int): Must be between 1 and 1000.

        Raises:
            ValueError: If the value is out of range.
        """
        IntValidator.validate_range(value, 1, 1000, "transparency")
        self._set_attr("transparency", value)

    @property
    def mosaic(self) -> bool:
        """
        Gets the mosaic flag for the watermark.

        Returns:
            bool: The current value. Default is False.
        """
        return self._get_attr("mosaic")

    @mosaic.setter
    def mosaic(self, value: bool):
        """
        Sets the mosaic flag for the watermark.

        Args:
            value (bool): Must be a boolean.

        Raises:
            TypeError: If value is not a boolean.
        """
        if not isinstance(value, bool):
            raise TypeError("Mosaic value must be a boolean.")
        self._set_attr("mosaic", value)

    @property
    def x_pos_percent(self) -> int:
        """
        Gets the x position percent for the watermark.

        Returns:
            int: The current value. Default is 0.
        """
        return self._get_attr("x_pos_percent")

    @x_pos_percent.setter
    def x_pos_percent(self, value: int):
        """
        Sets the x position percent for the watermark.

        Args:
            value (int): Must be between 0 and 100.

        Raises:
            ValueError: If the value is out of range.
        """
        IntValidator.validate_range(value, 0, 100, "x position percent")
        self._set_attr("x_pos_percent", value)

    @property
    def y_pos_percent(self) -> int:
        """
        Gets the y position percent for the watermark.

        Returns:
            int: The current value. Default is 0.
        """
        return self._get_attr("y_pos_percent")

    @y_pos_percent.setter
    def y_pos_percent(self, value: int):
        """
        Sets the y position percent for the watermark.

        Args:
            value (int): Must be between 0 and 100.

        Raises:
            ValueError: If the value is out of range.
        """
        IntValidator.validate_range(value, 0, 100, "y position percent")
        self._set_attr("y_pos_percent", value)

    @property
    def width_percent(self) -> int:
        """
        Gets the width percent for the watermark.

        Returns:
            int: The current value. Default is 100.
        """
        return self._get_attr("width_percent")

    @width_percent.setter
    def width_percent(self, value: int):
        """
        Sets the width percent for the watermark.

        Args:
            value (int): Must be between 0 and 100.

        Raises:
            ValueError: If the value is out of range.
        """
        IntValidator.validate_range(value, 0, 100, "width percent")
        self._set_attr("width_percent", value)

    @property
    def height_percent(self) -> int:
        """
        Gets the height percent for the watermark.

        Returns:
            int: The current value. Default is 100.
        """
        return self._get_attr("height_percent")

    @height_percent.setter
    def height_percent(self, value: int):
        """
        Sets the height percent for the watermark.

        Args:
            value (int): Must be between 0 and 100.

        Raises:
            ValueError: If the value is out of range.
        """
        IntValidator.validate_range(value, 0, 100, "height percent")
        self._set_attr("height_percent", value)

    def _set_image(self, file: File):
        """
        Internal method to set image file for watermark.

        Args:
            file (File): The image file.

        Raises:
            ValueError: If parent task is not set.
        """
        self._file = file
        if not self._parent_task:
            raise ValueError("Parent task must be set before setting image.")
        files = self._parent_task.files
        files.remove(file)
        self._payload["server_filename"] = file.server_filename

    def set_image(self, file_path: str) -> File:
        """
        Sets the image for image watermark.

        Args:
            file_path (str): Path to the image file.

        Returns:
            File: The added image file.

        Raises:
            TypeError: If watermark type is not "image".
            ValueError: If parent task is not set.
        """
        if self.type != "image":
            raise TypeError("This option is only available for image watermarks.")
        if not self._parent_task:
            raise ValueError("Parent task must be set before setting image.")

        file = self._parent_task.add_file(file_path)
        self._set_image(file)
        return file

    def _to_payload(self) -> dict:
        """
        Converts the element to payload for API.

        Returns:
            dict: The payload dictionary.
        """
        payload = super()._to_payload()
        if self.type == "text":
            payload.pop("image", None)
        if self.type == "image":
            payload.pop("text", None)
        return payload

    def _validate_payload(self, payload: dict):
        """
        Validates the payload for API.

        Args:
            payload (dict): The payload dictionary.

        Raises:
            ValueError: If required values are missing.
        """
        super()._validate_payload(payload)
        if payload["type"] == "text" and payload["text"] is None:
            raise ValueError("Text value must be provided for text watermark.")
        if payload["type"] == "image" and payload["server_filename"] is None:
            raise ValueError("Image value must be provided for image watermark.")


class WatermarkTask(Task):
    """
    Handles watermark tasks using the iLoveIMG API.

    Allows configuration and execution of watermarking for image files.

    Example:
        task = WatermarkTask(public_key="your_public_key", secret_key="your_secret_key")
        element = task.add_element()
        element.type = "text"
        element.text = "Sample Watermark"
    """

    _tool = "watermarkimage"

    _DEFAULT_PAYLOAD = {"elements": []}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.elements: list[WatermarkElement] = []

    def add_element(self, element: WatermarkElement | None = None) -> WatermarkElement:
        """
        Adds a watermark element to the task.

        Args:
            element (WatermarkElement | None): The element to add.

        Returns:
            WatermarkElement: The added element.
        """
        element = element or WatermarkElement(self)
        self.elements.append(element)
        return element

    def _to_payload(self) -> Payload:
        """
        Returns the serialized payload for the WatermarkTask.

        Returns:
            Payload: The payload dictionary.
        """
        self._payload["elements"] = self.elements
        return super()._to_payload()
