"""Unit tests for ResizeTask.

Verifies:
- Default attribute initialization.
- Validation of resize mode choices.
- Positive integer validation for pixel dimensions and percentage.
- Conditional required fields based on resize mode.
- Payload pruning logic in _to_payload().

These tests ensure the ResizeTask behaves correctly under different configuration
scenarios and raises the appropriate custom exceptions.
"""

import pytest

from iloveimg import ResizeTask
from iloveimg.exceptions import IntOutOfRangeError, InvalidChoiceError

from .base_test import AbstractUnitTaskTest


# pylint: disable=protected-access
class TestResizeTask(AbstractUnitTaskTest):
    """Unit test suite for the ResizeTask class."""

    _task_class = ResizeTask
    _task_tool = "resizeimage"

    def test_initialization(self, my_task):
        """
        Tests that a new ResizeTask instance initializes with expected
        default values.
        """
        assert my_task.resize_mode == "pixels"
        assert my_task.pixels_width is None
        assert my_task.pixels_height is None
        assert my_task.percentage is None
        assert my_task.maintain_ratio is True
        assert my_task.no_enlarge_if_smaller is True

    def test_set_resize_mode_valid(self, my_task):
        """
        Tests that valid resize modes ('pixels', 'percentage') are accepted and stored.
        """
        for mode in ("pixels", "percentage"):
            my_task.resize_mode = mode
            assert my_task.resize_mode == mode

    def test_set_resize_mode_invalid(self, my_task):
        """Tests that setting an invalid resize mode raises InvalidChoiceError."""
        with pytest.raises(InvalidChoiceError):
            my_task.resize_mode = "unknown"

    def test_set_pixels_dimensions(self, my_task):
        """
        Tests that pixel dimensions can be set and retrieved when resize_mode
        is 'pixels'.
        """
        my_task.resize_mode = "pixels"
        my_task.pixels_width = 100
        my_task.pixels_height = 200
        assert my_task.pixels_width == 100
        assert my_task.pixels_height == 200

    def test_pixels_dimensions_must_be_positive(self, my_task):
        """
        Tests that pixel dimensions must be positive integers; zero or negative
        raise IntOutOfRangeError.
        """
        my_task.resize_mode = "pixels"
        for pixels_width in (0, -1):
            with pytest.raises(IntOutOfRangeError):
                my_task.pixels_width = pixels_width
        for pixels_height in (0, -1):
            with pytest.raises(IntOutOfRangeError):
                my_task.pixels_height = pixels_height

    def test_resize_mode_is_pixels(self, my_task):
        """
        Tests that when resize_mode is 'pixels', both pixels_width and pixels_height
        are required."""
        my_task.resize_mode = "pixels"
        with pytest.raises(ValueError) as excinfo:
            my_task._to_payload()
        assert "pixels_width and pixels_height are required" in str(excinfo.value)

    def test_resize_mode_is_percentage(self, my_task):
        """
        Tests that when resize_mode is 'percentage', percentage is required and must be
        positive.
        """
        my_task.resize_mode = "percentage"
        with pytest.raises(ValueError) as excinfo:
            my_task._to_payload()
        assert "percentage is required" in str(excinfo.value)

        for percentage in (0, -1):
            with pytest.raises(IntOutOfRangeError):
                my_task.percentage = percentage

    def test_to_payload(self, my_task):
        """
        Tests that _to_payload() prunes fields not relevant to the chosen resize_mode.
        """
        my_task.resize_mode = "pixels"
        my_task.pixels_width = 100
        my_task.pixels_height = 200
        payload = my_task._to_payload()
        assert "percentage" not in payload

        my_task.resize_mode = "percentage"
        my_task.percentage = 20
        payload = my_task._to_payload()
        assert "pixels_width" not in payload
        assert "pixels_height" not in payload
