"""Unit tests for the RotateTask class in the iloveimg module.

These tests verify the correct behavior and parameter validation for image rotation
tasks using RotateTask.
"""

import pytest

from iloveimg import RotateTask
from iloveimg.exceptions import InvalidChoiceError
from iloveimg.rotate_task import ROTATE_ANGLE_OPTIONS, RotateFile

from .base_test import (
    AbstractUnitFileTest,
    AbstractUnitTaskTest,
)


class TestRotateFile(AbstractUnitFileTest):
    """Unit tests for the RotateFile class."""

    _task_class = RotateFile

    def test_initialization_sets_default_values(self, my_task):
        """
        Test that the RotateFile class initializes with default values.
        """
        assert ROTATE_ANGLE_OPTIONS == {0, 90, 180, 270}
        assert my_task._DEFAULT_PAYLOAD == {
            "rotate": 0,
        }
        assert my_task.rotate == 0

    @pytest.mark.parametrize("angle", ROTATE_ANGLE_OPTIONS)
    def test_set_rotation_valid_angles(self, my_task, angle):
        """
        Test that the RotateFile class sets the rotation angle correctly for valid
        angles.
        """
        my_task.rotate = angle
        assert my_task.rotate == angle

    @pytest.mark.parametrize("invalid_angle", [-90, 45, 100, 360, None, "90"])
    def test_set_rotation_invalid_angles(self, my_task, invalid_angle):
        """
        Test that the RotateFile class raises an InvalidChoiceError when setting
        an invalid rotation angle.
        """
        with pytest.raises(InvalidChoiceError):
            my_task.rotate = invalid_angle

    def test_to_payload_includes_rotate_angle(self, my_task):
        """
        Test that _to_payload includes the rotate angle.
        """
        my_task.rotate = 90
        payload = my_task._to_payload()
        assert "rotate" in payload
        assert payload["rotate"] == 90

    def test_multiple_rotation_angle_changes(self, my_task):
        """
        Test that rotation angle can be changed multiple times.
        """
        my_task.rotate = 90
        assert my_task.rotate == 90
        my_task.rotate = 180
        assert my_task.rotate == 180
        my_task.rotate = 270
        assert my_task.rotate == 270


class TestRotateTask(AbstractUnitTaskTest):
    """Unit tests for the RotateTask class."""

    _task_class = RotateTask
    _task_tool = "rotateimage"

    def test_init(self):
        """Test RotateTask initialization and inheritance."""
