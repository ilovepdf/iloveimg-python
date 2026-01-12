"""Helper functions and abstract base classes for the iloveimg-python library.

Provides base classes and utilities for serializing and validating payloads
for API requests.
"""

from typing import Any, Dict, Sequence

Payload = Dict[str, Any]


# pylint: disable=too-few-public-methods
class AbstractTaskElement:
    """Base class for task elements that can be serialized to an API payload.

    Example:
        class ExampleElement(AbstractTaskElement):
            _DEFAULT_PAYLOAD = {
                "attr1": "default_value_1",
                "attr2": "default_value_2",
            }

            @property
            def attr1(self) -> str:
                return self._get_attr("attr1")

            @attr1.setter
            def attr1(self, value: str):
                self._set_attr("attr1", value)

            # Usage:
            element = ExampleElement()
            element.attr1 = "custom_value"
            payload = element._to_payload()
    """

    _DEFAULT_PAYLOAD: Payload = {}
    _LIST_ATTRS: Sequence[str] = ("files", "elements")

    def __init__(self) -> None:
        self._payload: Payload = self._DEFAULT_PAYLOAD.copy()

    def _get_attr(self, key: str) -> Any:
        """Gets the value of an attribute from the payload.

        Args:
            key (str): The attribute key.

        Returns:
            Any: The value of the attribute.
        """
        return self._payload[key]

    def _set_attr(self, key: str, value: Any) -> None:
        """Sets the value of an attribute in the payload.

        Args:
            key (str): The attribute key.
            value (Any): The value to set.
        """
        self._payload[key] = value

    def _to_payload(self) -> Payload:
        """Returns a dict ready for the API.

        Recursively serializes items that expose `_to_payload()`.
        Runs `_validate_payload()` before returning.

        Returns:
            Payload: The serialized payload dictionary.

        Example:
            element = ExampleElement()
            payload = element._to_payload()
        """
        payload = self._serialize_lists(self._payload.copy())
        self._validate_payload(payload)
        return payload

    def _validate_payload(self, payload: Payload) -> None:
        """Validates the payload.

        Args:
            payload (Payload): The payload to validate.

        Raises:
            ValueError: If the payload is empty.
        """
        if not payload:
            raise ValueError("Payload cannot be empty.")

    @classmethod
    def _serialize_lists(cls, data: Payload) -> Payload:
        """Serializes list attributes in the payload by calling _to_payload.

        Args:
            data (Payload): The payload dictionary.

        Returns:
            Payload: The payload with serialized lists.
        """
        for key in cls._LIST_ATTRS:
            if key not in data:
                continue
            items = data[key]
            if not isinstance(items, Sequence) or isinstance(items, (str, bytes)):
                continue
            serialized = []
            for item in items:
                to_pl = getattr(item, "_to_payload", None)
                serialized.append(to_pl() if callable(to_pl) else item)
            data[key] = serialized
        return data
