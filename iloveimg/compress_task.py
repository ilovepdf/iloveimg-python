"""Handles image compression tasks using the iLoveIMG API.

Provides the CompressTask class to configure and execute image compression.
Allows optimization of images to reduce file size while maintaining quality.
"""

from typing import Literal

from .task import Task
from .validators import ChoiceValidator

CompressionLevelType = Literal["low", "recommended", "extreme"]
COMPRESSION_LEVEL_OPTIONS = {"low", "recommended", "extreme"}


class CompressTask(Task):
    """
    Handles image compression tasks using the iLoveIMG API.

    Args:
        public_key (str, optional): API public key.
            Uses ILOVEIMG_PUBLIC_KEY env variable if not provided.
        secret_key (str, optional): API secret key.
            Uses ILOVEIMG_SECRET_KEY env variable if not provided.
        make_start (bool, optional): Start the task immediately. Default is False.

    Example:
        task = CompressTask(public_key="your_public_key", secret_key="your_secret_key")
    """

    _tool = "compressimage"

    _DEFAULT_PAYLOAD = {
        "compression_level": "recommended",
    }

    @property
    def compression_level(self) -> CompressionLevelType:
        """
        Gets the current compression level.

        Returns:
            CompressionLevelType: The current value. Default is "recommended".
        """
        return self._get_attr("compression_level")

    @compression_level.setter
    def compression_level(self, value: CompressionLevelType):
        """
        Sets the compression level.

        Args:
            value (CompressionLevelType): Must be one of "low", "recommended",
                or "extreme".

        Raises:
            InvalidChoiceError: If value is not one of the allowed compression levels.
        """
        ChoiceValidator.validate(value, COMPRESSION_LEVEL_OPTIONS, "compression_level")
        self._set_attr("compression_level", value)
