"""Unit tests for the WatermarkTask class in the iloveimg module.

These tests verify the correct behavior and parameter validation for watermark tasks
using WatermarkTask.
"""

import pytest

from iloveimg import File, WatermarkElement, WatermarkTask
from iloveimg.exceptions import (
    IntOutOfRangeError,
    InvalidChoiceError,
    NotAnIntError,
)
from iloveimg.watermark_task import FONT_FAMILY_OPTIONS, GRAVITY_OPTIONS

from .base_test import (
    AbstractUnitTaskElementTest,
    AbstractUnitTaskTest,
)


class TestWatermarkElement(AbstractUnitTaskElementTest):
    """Test the WatermarkElement class."""

    _task_class = WatermarkElement

    def test_initialization(self, my_task):
        """
        Test that WatermarkElement is initialized correctly.

        Verifies that the default values are set correctly.
        """
        assert my_task.type == "text"
        assert my_task.text is None

        with pytest.raises(TypeError) as excinfo:
            print(my_task.server_filename)
        assert (
            "server_filename property is only available for image type watermark"
            in str(excinfo.value)
        )

        assert my_task.gravity == "Center"
        assert my_task.vertical_adjustment_percent == 0
        assert my_task.horizontal_adjustment_percent == 0
        assert my_task.rotation == 0
        assert my_task.font_family == "Arial"
        assert my_task.font_style is None
        assert my_task.font_size == 14
        assert my_task.font_color == "#000000"
        assert my_task.transparency == 100
        assert my_task.mosaic is False
        assert my_task.x_pos_percent == 0
        assert my_task.y_pos_percent == 0
        assert my_task.width_percent == 100
        assert my_task.height_percent == 100
        assert my_task._parent_task is None
        assert my_task._file is None

    def test_set_type(self, my_task):
        """Test setting watermark type and error for invalid type."""
        my_task.type = "text"
        assert my_task.type == "text"
        my_task.type = "image"
        assert my_task.type == "image"

        with pytest.raises(InvalidChoiceError):
            my_task.type = "invalid"

    def test_set_text(self, my_task):
        """Test setting watermark text and error for invalid text."""
        my_task.type = "text"
        my_task.text = "Hello World"
        assert my_task.text == "Hello World"

        with pytest.raises(TypeError) as excinfo:
            print(my_task.server_filename)
        assert (
            "server_filename property is only available for image type watermark."
            in str(excinfo.value)
        )

        with pytest.raises(TypeError) as excinfo:
            my_task.text = None
        assert "Invalid text value" in str(excinfo.value)

    def test_set_gravity(self, my_task):
        """
        Test setting the gravity of the watermark.

        Verifies that the gravity is set correctly and raises an error for invalid
        gravities.
        """

        for value in GRAVITY_OPTIONS:
            my_task.gravity = value
            assert my_task.gravity == value

        with pytest.raises(InvalidChoiceError):
            my_task.gravity = "invalid"

    def test_set_vertical_adjustment_percent(self, my_task):
        """
        Test setting the vertical adjustment percent of the watermark.

        Verifies that the vertical adjustment percent is set correctly and raises an
        error for invalid values.
        """

        for value in range(-100, 101):
            my_task.vertical_adjustment_percent = value
            assert my_task.vertical_adjustment_percent == value

        with pytest.raises(IntOutOfRangeError):
            my_task.vertical_adjustment_percent = -101

        with pytest.raises(IntOutOfRangeError):
            my_task.vertical_adjustment_percent = 101

        with pytest.raises(NotAnIntError):
            my_task.vertical_adjustment_percent = 1.1

    def test_set_horizontal_adjustment_percent(self, my_task):
        """
        Test setting the horizontal adjustment percent of the watermark.

        Verifies that the horizontal adjustment percent is set correctly and raises an
        error for invalid values.
        """

        for value in range(-100, 101):
            my_task.horizontal_adjustment_percent = value
            assert my_task.horizontal_adjustment_percent == value

        with pytest.raises(IntOutOfRangeError):
            my_task.horizontal_adjustment_percent = -101

        with pytest.raises(IntOutOfRangeError):
            my_task.horizontal_adjustment_percent = 101

        with pytest.raises(NotAnIntError):
            my_task.horizontal_adjustment_percent = 1.1

    def test_set_rotation(self, my_task):
        """
        Test setting the rotation of the watermark.

        Verifies that the rotation is set correctly and raises an error for invalid
        values.
        """

        for value in range(0, 360):
            my_task.rotation = value
            assert my_task.rotation == value

        for rotation in (-101, -1, 361):
            with pytest.raises(IntOutOfRangeError):
                my_task.rotation = rotation

        with pytest.raises(NotAnIntError):
            my_task.rotation = 1.1

    def test_set_font_family(self, my_task):
        """Test setting the font family."""
        for value in FONT_FAMILY_OPTIONS:
            my_task.font_family = value
            assert my_task.font_family == value
        with pytest.raises(InvalidChoiceError):
            my_task.font_family = "Unknown"

    def test_font_style(self, my_task):
        """Test setting the font style."""
        my_task.font_style = None
        assert my_task.font_style is None
        my_task.font_style = "Bold"
        assert my_task.font_style == "Bold"
        my_task.font_style = "Italic"
        assert my_task.font_style == "Italic"

        with pytest.raises(InvalidChoiceError):
            my_task.font_style = "Unknown"

    def test_font_size(self, my_task):
        """Test setting the font size."""
        my_task.font_size = 12
        assert my_task.font_size == 12

        with pytest.raises(IntOutOfRangeError):
            my_task.font_size = -1

        with pytest.raises(NotAnIntError):
            my_task.font_size = "Unknown"

    def test_transparency(self, my_task):
        """Test setting the transparency."""
        my_task.transparency = 500
        assert my_task.transparency == 500

        with pytest.raises(NotAnIntError):
            my_task.transparency = "Unknown"

        for value in (-1, 0, 1001):
            with pytest.raises(IntOutOfRangeError):
                my_task.transparency = value

    def test_set_mosaic(self, my_task):
        """Test setting the mosaic property."""
        my_task.mosaic = True
        assert my_task.mosaic is True
        my_task.mosaic = False
        assert my_task.mosaic is False
        with pytest.raises(TypeError) as excinfo:
            my_task.mosaic = "not_bool"
        assert "Mosaic value must be a boolean" in str(excinfo.value)

    def test_set_image(self, my_task):
        """Test setting the image property (if implemented)."""
        my_task.type = "image"
        my_task._payload["server_filename"] = "image.png"
        assert my_task.server_filename == "image.png"

        with pytest.raises(TypeError) as excinfo:
            print(my_task.text)
        assert "Text property is only available for text type watermark" in str(
            excinfo.value
        )

    def test_to_payload_type_text(self, my_task):
        """Test getting file options for text type watermark."""

        my_task.type = "text"
        with pytest.raises(ValueError) as excinfo:
            my_task._to_payload()
        assert "Text value must be provided for text watermark" in str(excinfo.value)

        my_task.text = "Hello, World!"

        options = my_task._to_payload()
        assert "image" not in options

    def test_to_payload_type_image(self, my_task):
        """Test getting file options for image type watermark."""

        my_task.type = "image"
        with pytest.raises(ValueError):
            my_task._to_payload()

        my_task._payload["server_filename"] = "image.jpg"
        options = my_task._to_payload()
        assert "text" not in options

    def test_set_x_pos_percent(self, my_task):
        """
        Test setting the x position percent of the watermark.

        Verifies that the x position percent is set correctly and raises an error for
        invalid values.
        """

        for value in range(0, 101):
            my_task.x_pos_percent = value
            assert my_task.x_pos_percent == value

        with pytest.raises(NotAnIntError):
            my_task.x_pos_percent = 1.1

        with pytest.raises(IntOutOfRangeError):
            my_task.x_pos_percent = -1

        with pytest.raises(IntOutOfRangeError):
            my_task.x_pos_percent = 101

    def test_set_y_pos_percent(self, my_task):
        """
        Test setting the y position percent of the watermark.

        Verifies that the y position percent is set correctly and raises an error for
        invalid values.
        """

        for value in range(0, 101):
            my_task.y_pos_percent = value
            assert my_task.y_pos_percent == value

        with pytest.raises(NotAnIntError):
            my_task.y_pos_percent = 1.1

        with pytest.raises(IntOutOfRangeError):
            my_task.y_pos_percent = -1

        with pytest.raises(IntOutOfRangeError):
            my_task.y_pos_percent = 101

    def test_set_width_percent(self, my_task):
        """
        Test setting the width percent of the watermark.

        Verifies that the width percent is set correctly and raises an error for invalid
        values.
        """

        for value in range(0, 101):
            my_task.width_percent = value
            assert my_task.width_percent == value

        with pytest.raises(NotAnIntError):
            my_task.width_percent = 1.1

        with pytest.raises(IntOutOfRangeError):
            my_task.width_percent = -1

        with pytest.raises(IntOutOfRangeError):
            my_task.width_percent = 101

    def test_set_height_percent(self, my_task):
        """
        Test setting the height percent of the watermark.

        Verifies that the height percent is set correctly and raises an error for
        invalid values.
        """

        for value in range(0, 101):
            my_task.height_percent = value
            assert my_task.height_percent == value

        with pytest.raises(NotAnIntError):
            my_task.height_percent = 1.1

        with pytest.raises(IntOutOfRangeError):
            my_task.height_percent = -1

        with pytest.raises(IntOutOfRangeError):
            my_task.height_percent = 101

    def test_set_type_image(self, my_task):
        """
        Test setting the file for the watermark.

        Verifies that the file is set correctly and raises an error for invalid values.
        """

        assert my_task._file is None

        with pytest.raises(TypeError) as excinfo:
            my_task.set_image("sample.jpg")
        assert "This option is only available for image watermarks" in str(
            excinfo.value
        )


class TestWatermarkTask(AbstractUnitTaskTest):
    """
    Unit tests for the WatermarkTask class.

    These tests verify correct initialization and configuration for watermark tasks,
    ensuring that watermarking options are set and validated as expected.
    """

    _task_class = WatermarkTask
    _task_tool = "watermarkimage"

    def test_initialization(self, my_task):
        """Test initialization of the WatermarkTask class."""
        assert my_task.elements == []

    def test_add_element(self, my_task):
        """Test adding elements to the WatermarkTask class."""
        element = my_task.add_element()  # type: ignore
        assert isinstance(element, WatermarkElement)
        assert my_task is element._parent_task

        element1 = my_task.add_element()  # type: ignore

        element2 = my_task.add_element()  # type: ignore

        assert len(my_task.elements) == 3  # type: ignore
        assert my_task.elements == [element, element1, element2]

    def test_add_element_image(self, my_task):
        """Test adding image elements to the WatermarkTask class."""
        element = my_task.add_element()
        element.type = "image"

        for i in (0, 1):
            server_filename = f"server_filename{i}.png"
            filename = f"filename{i}.png"
            file = File(server_filename, filename)
            my_task.append_file(file)
            element._set_image(file)
            assert element._file is file
            assert file not in my_task.files
            assert element._payload["server_filename"] == server_filename
