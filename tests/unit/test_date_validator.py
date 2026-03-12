"""Unit tests for DateValidator covering formats and range validation.

These tests ensure the validator accepts all supported formats, enforces proper
types, and respects optional minimum/maximum boundaries for date strings.
"""

import re
from typing import Any

import pytest

from iloveimg.validators.date_validator import DATE_FORMATS, DateValidator


class TestDateValidator:
    """Test suite for DateValidator."""

    @pytest.mark.parametrize(
        "date_str",
        [
            "01-12-2024",
            "01/12/2024",
            "01.12.2024",
            "2024-12-01",
            "2024/12/01",
            "2024.12.01",
            "12-01-2024",
            "12/01/2024",
            "12.01.2024",
        ],
    )
    def test_validate_format_accepts_supported_formats(self, date_str) -> None:
        """Accepted formats should pass without raising errors."""
        DateValidator.validate_format(date_str)

    def test_validate_format_rejects_non_string(self) -> None:
        """Non-string values must raise TypeError."""
        invalid_value: Any = 20240101
        with pytest.raises(TypeError, match="Value must be a string."):
            DateValidator.validate_format(invalid_value)

    def test_validate_format_rejects_unknown_format(self) -> None:
        """Dates outside the supported formats must raise ValueError."""
        with pytest.raises(ValueError, match=re.escape(str(DATE_FORMATS))):
            DateValidator.validate_format("2024*12*01", "start_date")

    def test_validate_in_range_accepts_within_boundaries(self) -> None:
        """validate_in_range should allow dates within min/max inclusive."""
        DateValidator.validate_in_range(
            "2024-05-15", min_date="2024-05-01", max_date="2024-05-31"
        )
        DateValidator.validate_in_range("2024-05-01", min_date="2024-05-01")
        DateValidator.validate_in_range("2024-05-31", max_date="2024-05-31")

    def test_validate_in_range_rejects_below_min(self) -> None:
        """Dates earlier than min_date should raise ValueError."""
        with pytest.raises(
            ValueError, match="Date for release must be on or after 2024-05-01."
        ):
            DateValidator.validate_in_range(
                "2024-04-30", min_date="2024-05-01", param_name="release"
            )

    def test_validate_in_range_rejects_above_max(self) -> None:
        """Dates later than max_date should raise ValueError."""
        with pytest.raises(ValueError, match="Date must be on or before 2024-05-31."):
            DateValidator.validate_in_range(
                "2024-06-01", max_date="2024-05-31", param_name=None
            )

    def test_validate_in_range_rejects_invalid_string(self) -> None:
        """Invalid date strings should raise due to failed parsing."""
        with pytest.raises(ValueError, match=re.escape(str(DATE_FORMATS))):
            DateValidator.validate_in_range("31-02-2024")

    def test_parse_date_private_helper_via_in_range(self) -> None:
        """Ensure _parse_date path is exercised with non-default formats."""
        DateValidator.validate_in_range(
            "01/06/2024", min_date="01/05/2024", max_date="30/06/2024"
        )
