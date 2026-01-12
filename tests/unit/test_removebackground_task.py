"""Test the RemoveBackgroundTask class."""

from iloveimg import RemoveBackgroundTask

from .base_test import AbstractUnitTaskTest


class TestRemoveBackgroundTask(AbstractUnitTaskTest):
    """Test the RemoveBackgroundTask class."""

    _task_class = RemoveBackgroundTask
    _task_tool = "removebackgroundimage"
