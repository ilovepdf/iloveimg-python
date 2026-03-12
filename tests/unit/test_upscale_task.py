"""Unit tests for the UpScaleTask class in the iloveimg module.

These tests verify the correct behavior and parameter validation for image upscaling
tasks using UpScaleTask.
"""

import pytest

from iloveimg import UpScaleTask
from iloveimg.exceptions import IntNotInAllowedSetError

from .base_test import AbstractUnitTaskTest


class TestUpScaleTask(AbstractUnitTaskTest):
    """
    Unit tests for UpScaleTask.

    Covers initialization, valid and invalid multiplier settings,
    and parameter validation.
    """

    _task_class = UpScaleTask
    _task_tool = "upscaleimage"

    def test_initialization(self, my_task):
        """
        Verify UpScaleTask initialization.

        Ensures default upscale parameters are correctly initialized.
        """
        assert my_task.multiplier is None

    @pytest.mark.parametrize("multiplier", [2, 4])
    def test_set_multiplier_valid(self, my_task, multiplier):
        """
        Test setting valid upscale multiplier values.

        Verifies that the multiplier can be set to allowed values (2 or 4).
        """
        my_task.multiplier = multiplier
        assert my_task.multiplier == multiplier

    @pytest.mark.parametrize("multiplier", [6, -2])
    def test_set_multipliers_invalid(self, my_task, multiplier):
        """
        Test setting invalid upscale multiplier values.

        Verifies that setting a multiplier outside the allowed set raises an
            exception.
        """
        with pytest.raises(IntNotInAllowedSetError) as excinfo:
            my_task.multiplier = multiplier
        assert "Invalid value `multiplier`: value must be one" in str(excinfo.value)
