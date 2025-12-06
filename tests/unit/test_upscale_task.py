"""Test the UpScaleTask class."""

import pytest

from iloveimg import UpScaleTask
from iloveimg.exceptions import IntNotInAllowedSetError

from .base_test import AbstractUnitTaskTest


class TestUpScaleTask(AbstractUnitTaskTest):
    """Test the UpScaleTask class."""

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
        Test setting valid upscale dimensions.

        Verifies that width, height, x, and y can be set to valid values.
        """
        my_task.multiplier = multiplier
        assert my_task.multiplier == multiplier

    @pytest.mark.parametrize("multiplier", [6, -2])
    def test_set_multipliers_invalid(self, my_task, multiplier):
        """
        Test setting invalid upscale dimensions.

        Verifies that setting invalid values for width, height, x, or y raises an
            exception.
        """
        with pytest.raises(IntNotInAllowedSetError) as excinfo:
            my_task.multiplier = multiplier
        assert "Invalid value `multiplier`: value must be one" in str(excinfo.value)
