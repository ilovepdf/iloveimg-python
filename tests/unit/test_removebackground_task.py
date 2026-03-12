"""Unit tests for the RemoveBackgroundTask class in the iloveimg module.

These tests verify the correct behavior and initialization for image background
removal tasks using RemoveBackgroundTask.
"""

from iloveimg import RemoveBackgroundTask

from .base_test import AbstractUnitTaskTest


class TestRemoveBackgroundTask(AbstractUnitTaskTest):
    """
    Unit tests for RemoveBackgroundTask.

    Covers initialization and tool configuration for background removal tasks.
    """

    _task_class = RemoveBackgroundTask
    _task_tool = "removebackgroundimage"
