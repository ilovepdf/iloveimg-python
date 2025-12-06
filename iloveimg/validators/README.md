# Validators Module

## Overview

The `validators` module provides reusable validator classes for validating various parameter types and values used throughout the iloveimg-python library.

## Validators

### IntValidator

Validates integer values with various constraints.

**Methods:**
- `validate_type(value, param_name)` - Ensure value is an integer
- `validate_positive(value, param_name)` - Ensure value is a positive integer (> 0)
- `validate_range(value, min_value, max_value, param_name)` - Ensure value is within range
- `validate_options(value, options, param_name)` - Ensure value is in allowed set

**Example:**
```python
from iloveimg.validators import IntValidator

# Validate type
IntValidator.validate_type(5)  # OK
IntValidator.validate_type("5")  # Raises NotAnIntError

# Validate positive
IntValidator.validate_positive(10, "width")  # OK
IntValidator.validate_positive(0, "width")  # Raises IntOutOfRangeError

# Validate range
IntValidator.validate_range(50, 1, 100, "quality")  # OK
IntValidator.validate_range(150, 1, 100, "quality")  # Raises IntOutOfRangeError

# Validate options
IntValidator.validate_options(90, {0, 90, 180, 270}, "rotation")  # OK
IntValidator.validate_options(45, {0, 90, 180, 270}, "rotation")  # Raises IntNotInAllowedSetError
```

### ChoiceValidator

Validates that values are among a set of allowed choices.

**Methods:**
- `validate(value, allowed, param_name, cls_error)` - Ensure value is in allowed choices

**Parameters:**
- `value` (Any): The value to validate
- `allowed` (Iterable[Any]): Set of allowed values
- `param_name` (str, optional): Parameter name for error messages. Default: "parameter"
- `cls_error` (Type[Exception], optional): Exception class to raise. Default: InvalidChoiceError

**Example:**
```python
from iloveimg.validators import ChoiceValidator
from iloveimg.exceptions import InvalidChoiceError

# Validate with default error
ChoiceValidator.validate("jpg", ["jpg", "png", "gif"], "format")  # OK
ChoiceValidator.validate("bmp", ["jpg", "png", "gif"], "format")  # Raises InvalidChoiceError

# Validate with custom error
from iloveimg.exceptions import IntNotInAllowedSetError

ChoiceValidator.validate(
    90,
    {0, 90, 180, 270},
    "rotation",
    cls_error=IntNotInAllowedSetError
)  # OK or raises IntNotInAllowedSetError
```

## Exceptions

Validators use the following exceptions from `iloveimg.exceptions`:

- `NotAnIntError` - Raised when a value is not an integer
- `IntOutOfRangeError` - Raised when an integer is outside the allowed range
- `IntNotInAllowedSetError` - Raised when an integer is not in the allowed set
- `InvalidChoiceError` - Raised when a value is not among allowed choices

## Usage in Tasks

Validators are used internally by task classes to validate parameters:

```python
from iloveimg.compress_task import CompressTask

task = CompressTask(public_key="your_key", secret_key="your_secret")
task.compression_level = "low"  # Uses validators internally
```



## Performance Considerations

- All validators are implemented as static methods for minimal overhead
- Validators use simple type checking and comparison
- No caching or memoization (validation is lightweight)
- Suitable for frequent validation calls

## Future Extensions

Additional validators can be easily added following the same pattern:

```python
# Example: StringValidator (to be added)
class StringValidator:
    @staticmethod
    def validate_length(value, min_len, max_len, param_name):
        # Implementation
        pass

    @staticmethod
    def validate_pattern(value, pattern, param_name):
        # Implementation
        pass

# Example: DateValidator (to be added)
class DateValidator:
    @staticmethod
    def validate_in_range(value, min_date, max_date, param_name):
        # Implementation
        pass
```

## Testing

Each validator has comprehensive unit tests in `tests/unit/`:
- `test_int_validator.py` - Tests for IntValidator
- `test_choice_validator.py` - Tests for ChoiceValidator

Run tests with:
```bash
pytest tests/unit/test_int_validator.py -v
pytest tests/unit/test_choice_validator.py -v
```

## See Also

- `iloveimg/abstract_task_element.py` - AbstractTaskElement base class
- `iloveimg/exceptions/` - Exception definitions
- `tests/unit/` - Validator tests
```
