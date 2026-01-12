"""Unit tests for the CropTask class."""

from unittest.mock import MagicMock

import pytest

from iloveimg import CropTask, File
from iloveimg.exceptions import IntOutOfRangeError, NotAnIntError

from .base_test import AbstractUnitTaskTest


# pylint: disable=protected-access
class TestCropTask(AbstractUnitTaskTest):
    """Test the CropTask class."""

    _task_class = CropTask
    _task_tool = "cropimage"

    def test_initialization(self, my_task):
        """Test that CropTask initializes with correct default values."""
        assert my_task._DEFAULT_PAYLOAD == {
            "width": None,
            "height": None,
            "x": 0,
            "y": 0,
        }
        assert my_task.width is None
        assert my_task.height is None
        assert my_task.x == 0
        assert my_task.y == 0

    def test_width_property(self, my_task):
        """Test width property getter and setter with valid values."""
        my_task.width = 400
        assert my_task.width == 400

        my_task.width = 1
        assert my_task.width == 1

    def test_width_invalid_values(self, my_task):
        """Test width property rejects invalid values."""
        # Zero should raise error
        with pytest.raises(IntOutOfRangeError) as excinfo:
            my_task.width = 0
        assert "Invalid width: value must be a positive integer" in str(excinfo.value)

        # Negative should raise error
        with pytest.raises(IntOutOfRangeError) as excinfo:
            my_task.width = -100
        assert "Invalid width: value must be a positive integer" in str(excinfo.value)

        # Non-integer should raise error
        with pytest.raises(NotAnIntError) as excinfo:
            my_task.width = "400"
        assert "Invalid width: value must be an integer" in str(excinfo.value)

    def test_height_property(self, my_task):
        """Test height property getter and setter with valid values."""
        my_task.height = 300
        assert my_task.height == 300

        my_task.height = 1
        assert my_task.height == 1

    def test_height_invalid_values(self, my_task):
        """Test height property rejects invalid values."""
        # Zero should raise error
        with pytest.raises(IntOutOfRangeError) as excinfo:
            my_task.height = 0
        assert "Invalid height: value must be a positive integer" in str(excinfo.value)

        # Negative should raise error
        with pytest.raises(IntOutOfRangeError) as excinfo:
            my_task.height = -200
        assert "Invalid height: value must be a positive integer" in str(excinfo.value)

        # Non-integer should raise error
        with pytest.raises(NotAnIntError) as excinfo:
            my_task.height = 300.5
        assert "Invalid height: value must be an integer" in str(excinfo.value)

    def test_x_property(self, my_task):
        """Test x property getter and setter with valid values."""
        my_task.x = 50
        assert my_task.x == 50

        my_task.x = 1
        assert my_task.x == 1

    def test_x_invalid_values(self, my_task):
        """Test x property rejects invalid values."""
        # Zero should raise error
        with pytest.raises(IntOutOfRangeError) as excinfo:
            my_task.x = 0
        assert "Invalid x: value must be a positive integer" in str(excinfo.value)

        # Negative should raise error
        with pytest.raises(IntOutOfRangeError) as excinfo:
            my_task.x = -10
        assert "Invalid x: value must be a positive integer" in str(excinfo.value)

    def test_y_property(self, my_task):
        """Test y property getter and setter with valid values."""
        my_task.y = 50
        assert my_task.y == 50

        my_task.y = 1
        assert my_task.y == 1

    def test_y_invalid_values(self, my_task):
        """Test y property rejects invalid values."""
        # Zero should raise error
        with pytest.raises(IntOutOfRangeError) as excinfo:
            my_task.y = 0
        assert "Invalid y: value must be a positive integer" in str(excinfo.value)

        # Negative should raise error
        with pytest.raises(IntOutOfRangeError) as excinfo:
            my_task.y = -20
        assert "Invalid y: value must be a positive integer" in str(excinfo.value)

    def test_to_payload(self, my_task):
        """Test that _to_payload returns correct payload structure."""
        my_task.width = 400
        my_task.height = 300
        my_task.x = 100
        my_task.y = 200

        payload = my_task._to_payload()
        assert payload == {
            "tool": "cropimage",
            "width": 400,
            "height": 300,
            "x": 100,
            "y": 200,
            "files": [],
        }

    def test_validate_payload_requires_width(self, my_task):
        """Test that _validate_payload raises error when width is not set."""
        my_task.height = 300
        my_task.x = 100
        my_task.y = 200

        with pytest.raises(ValueError) as excinfo:
            my_task._to_payload()
        assert "Width must be specified" in str(excinfo.value)

    def test_validate_payload_requires_height(self, my_task):
        """Test that _validate_payload raises error when height is not set."""
        my_task.width = 400
        my_task.x = 100
        my_task.y = 200

        with pytest.raises(ValueError) as excinfo:
            my_task._to_payload()
        assert "Height must be specified" in str(excinfo.value)

    def test_append_single_file(self, my_task):
        """Test that a single file can be appended to the task."""

        mock_file = MagicMock(spec=File)
        mock_file.server_filename = "server_file.jpg"
        mock_file.filename = "local_file.jpg"

        my_task.append_file(mock_file)

        assert len(my_task.files) == 1
        assert my_task.files[0] == mock_file

    def test_append_multiple_files_not_allowed(self, my_task):
        """Test that appending a second file raises ValueError."""

        mock_file1 = MagicMock(spec=File)
        mock_file2 = MagicMock(spec=File)

        my_task.append_file(mock_file1)

        with pytest.raises(ValueError) as excinfo:
            my_task.append_file(mock_file2)
        assert "CropTask only supports a single file" in str(excinfo.value)
