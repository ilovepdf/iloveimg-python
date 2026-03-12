"""Unit tests for FloatValidator covering type, positivity, range, and options.

These tests validate float inputs to ensure proper type, range, positivity,
and allowed-option enforcement across tasks.
"""

import math

import pytest

from iloveimg.exceptions import FloatOutOfRangeError, InvalidChoiceError
from iloveimg.validators.float_validator import FloatValidator


class TestFloatValidator:
    """
    Tests for FloatValidator.

    Covers:
    - Type validation for floats and ints
    - Positive-only enforcement
    - Inclusive range boundaries
    - Allowed value options
    """

    def test_validate_type_accepts_float_and_int(self) -> None:
        """Valid values should pass without raising errors."""
        FloatValidator.validate_type(1.25)
        FloatValidator.validate_type(0.0)
        FloatValidator.validate_type(5)  # ints should be accepted as floats

    @pytest.mark.parametrize(
        ("value", "name"),
        [
            ("1.5", None),
            (None, "scale"),
            ([], "ratio"),
        ],
    )
    def test_validate_type_rejects_non_numeric(self, value, name) -> None:
        """
        Ensure non float/int values raise TypeError including the given name.
        """
        with pytest.raises(TypeError):
            FloatValidator.validate_type(value, name)

    def test_validate_positive_accepts_positive_values(self) -> None:
        """Positive floats should be accepted."""
        FloatValidator.validate_positive(0.0001)
        FloatValidator.validate_positive(10.5, "zoom")

    @pytest.mark.parametrize(
        ("value", "expected"),
        [
            (0, "Value for exposure must be a positive float."),
            (-0.1, "Value must be a positive float."),
        ],
    )
    def test_validate_positive_rejects_zero_or_negative(self, value, expected) -> None:
        """Zero or negative values must raise FloatOutOfRangeError."""
        param_name = "exposure" if "for exposure" in expected else None
        with pytest.raises(FloatOutOfRangeError, match=expected):
            FloatValidator.validate_positive(value, param_name)

    def test_validate_range_accepts_bounds_inclusive(self) -> None:
        """Values equal to min or max should pass range validation."""
        FloatValidator.validate_range(0.5, 0.5, 1.0, "opacity")
        FloatValidator.validate_range(1.0, 0.5, 1.0, "opacity")
        FloatValidator.validate_range(0.75, 0.5, 1.0)

    @pytest.mark.parametrize(
        ("value", "min_value", "max_value", "message"),
        [
            (0.25, 0.5, 1.0, "Value for opacity must be between 0.5 and 1.0."),
            (1.5, 0.2, 1.0, "Value must be between 0.2 and 1.0."),
        ],
    )
    def test_validate_range_rejects_out_of_bounds(
        self, value, min_value, max_value, message
    ) -> None:
        """Out-of-range values should raise FloatOutOfRangeError."""
        param_name = "opacity" if "for opacity" in message else None
        with pytest.raises(FloatOutOfRangeError, match=message):
            FloatValidator.validate_range(value, min_value, max_value, param_name)

    def test_validate_options_accepts_allowed_value(self) -> None:
        """Allowed values should pass options validation."""
        FloatValidator.validate_options(1.5, {0.5, 1.0, 1.5}, "scale")

    def test_validate_options_rejects_disallowed_value(self) -> None:
        """Values outside the options set should raise InvalidChoiceError."""
        with pytest.raises(
            InvalidChoiceError,
            match=(
                r"Invalid value for quality: must be one of "
                r"\[0\.5, 0\.8, 1\.0\]\."
            ),
        ):
            FloatValidator.validate_options(0.7, {1.0, 0.8, 0.5}, "quality")

    def test_validate_type_outputs_actual_type_in_message(self) -> None:
        """The error message should embed the actual Python type name."""
        with pytest.raises(
            TypeError,
            match="Value for ratio must be a float.<class 'str'>",
        ):
            FloatValidator.validate_type("bad", "ratio")

    def test_validate_range_handles_nan(self) -> None:
        """NaN should be rejected during type validation before range comparison."""
        with pytest.raises(FloatOutOfRangeError):
            FloatValidator.validate_range(math.nan, 0.0, 1.0, "intensity")
