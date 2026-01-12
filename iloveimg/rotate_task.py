"""Handles image rotation tasks using the iLoveIMG API.

Provides classes to configure and execute rotation of image files.
Allows specifying rotation angles for each file.
"""

from typing import Literal

from .file import File
from .task import Task
from .validators import ChoiceValidator

RotationAngleType = Literal[0, 90, 180, 270]
ROTATE_ANGLE_OPTIONS = {0, 90, 180, 270}


class RotateFile(File):
    """
    Represents a file for the rotate task.

    Example:
        file = RotateFile()
        file.rotate = 90
    """

    _DEFAULT_PAYLOAD = {
        "rotate": 0,
    }

    @property
    def rotate(self) -> RotationAngleType:
        """
        Gets the rotation angle.

        Returns:
            RotationAngleType: The current value. Default is 0.
        """
        return self._get_attr("rotate")

    @rotate.setter
    def rotate(self, value: RotationAngleType):
        """
        Sets the rotation angle.

        Args:
            value (RotationAngleType): Must be one of 0, 90, 180, 270.

        Raises:
            InvalidChoiceError: If value is not one of the allowed angles.
        """
        ChoiceValidator.validate(value, ROTATE_ANGLE_OPTIONS, "rotate")
        self._set_attr("rotate", value)


class RotateTask(Task):
    """
    Handles the image rotate task using the iLoveIMG API.

    Example:
        task = RotateTask(public_key="your_public_key", secret_key="your_secret_key")
        file = task.add_file(path="image.jpg", rotate=90)
    """

    _tool = "rotateimage"
    cls_file: type[RotateFile] = RotateFile

    def add_file(self, *args, **kwargs) -> RotateFile:
        """
        Adds a file to the rotate task.

        Returns:
            RotateFile: The file object added to the task.
        """
        file = super().add_file(*args, **kwargs)
        rotate = kwargs.get("rotate")
        if rotate is not None:
            file.rotate = rotate

        return file
