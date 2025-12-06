"""Module for handling image background removal tasks using the iLoveIMG API.

This module provides a class to configure and execute the removal of backgrounds
from one or more image files.
"""

from .task import Task


class RemoveBackgroundTask(Task):
    """
    Class to handle the image background removal task using the iLoveIMG API.

    This class allows you to configure and execute the removal of backgrounds from one
    or more image files.
    """

    _tool = "removebackgroundimage"
