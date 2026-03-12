# iloveimg Core Library

This folder contains the core Python source code for interacting with the iLoveIMG API. All main classes, utilities, and logic for handling image processing tasks (such as compressing, resizing, converting, cropping, and more) are implemented here.

## Structure

- Each module is focused on a specific task or functionality.
- Shared utilities and base classes are organized for reuse and clarity.
- All public classes and methods include type annotations and module-level docstrings.

### Main Modules

| Module                       | Description                                      |
|------------------------------|--------------------------------------------------|
| `compress_task.py`           | Compress images to reduce file size.             |
| `convert_task.py`            | Convert images between formats.                  |
| `crop_task.py`               | Crop images using coordinates or presets.        |
| `removebackground_task.py`   | Remove background from images.                   |
| `resize_task.py`             | Resize images by width, height, or percentage.   |
| `rotate_task.py`             | Rotate images by specified angles.               |
| `upscale_task.py`            | Upscale images using AI.                         |
| `watermark_task.py`          | Add text or image watermarks to images.          |

#### Other Modules

- `file.py`: File handling utilities for tasks.
- `abstract_task_element.py`: AbstractTaskElement base class.
- `iloveimg_api.py`: Core API communication logic.
- `task.py`: Base class for all tasks.
- `exceptions/`: Custom exception classes.
- `validators/`: Input validation utilities.

## Development Guidelines

- Keep the code modular and well-documented.
- Ensure all new modules and classes include appropriate docstrings (Google style, in English).
- Any file ending with `*_task.py` must have corresponding unit and integration tests, as well as a sample script.
- Use type hints for all public methods and properties.
- Follow PEP 8 and project-specific naming conventions.
- Use the provided validators for input validation in tasks and models.

## Related Documentation

- [Project Overview](../README.md)
- [Samples and Usage](../samples/README.md)
- [Testing](../tests/README.md)
- [Docker and Environment Setup](../.docker/README.md)

For the official API documentation, visit: [iLoveIMG API Docs](https://developer.iloveimg.com/docs)
