"""Custom exceptions for invalid task configurations.

Defines TaskConfigurationError for scenarios where task parameters break
required constraints.
"""


class TaskConfigurationError(ValueError):
    """
    Raised when a task configuration violates required constraints.

    Args:
        message (str, optional): Custom error description.
            Defaults to "Invalid task configuration.".

    Example:
        raise TaskConfigurationError(
            "gif_time can only be set when convert_to is 'gif_animation'."
        )
    """

    def __init__(self, message: str = "Invalid task configuration."):
        super().__init__(message)
