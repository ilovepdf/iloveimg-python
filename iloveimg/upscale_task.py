"""Handles image upscaling tasks using the iLoveIMG API.

Provides the UpScaleTask class to configure and execute image upscaling,
allowing you to increase the resolution and quality of image files.
"""

from typing import Literal

from .abstract_task_element import Payload
from .task import Task
from .validators import IntValidator

MultiplierType = Literal[2, 4]
MULTIPLIER_OPTIONS = {2, 4}


class UpScaleTask(Task):
    """
    Handles image upscaling tasks using the iLoveIMG API.

    Args:
        public_key (str, optional): API public key.
            Uses ILOVEIMG_PUBLIC_KEY env variable if not provided.
        secret_key (str, optional): API secret key.
            Uses ILOVEIMG_SECRET_KEY env variable if not provided.
        make_start (bool, optional): Start the task immediately. Default is False.

    Example:
        task = UpScaleTask(public_key="your_public_key", secret_key="your_secret_key")
    """

    _tool = "upscaleimage"

    _DEFAULT_PAYLOAD = {
        "multiplier": None,
    }

    @property
    def multiplier(self) -> MultiplierType:
        """
        Gets the multiplier.

        Returns:
            MultiplierType: The current value. Default is None.
        """
        return self._get_attr("multiplier")

    @multiplier.setter
    def multiplier(self, value: MultiplierType):
        """
        Sets the multiplier.

        Args:
            value (MultiplierType): Must be one of 2 or 4.

        Raises:
            IntNotInAllowedSetError: If value is not one of the allowed multipliers.
        """
        IntValidator.validate_options(value, MULTIPLIER_OPTIONS, "multiplier")
        self._set_attr("multiplier", value)

    def _validate_payload(self, payload: Payload) -> None:
        super()._validate_payload(payload)
        if payload.get("multiplier") is None:
            raise ValueError("Multiplier must be specified")
