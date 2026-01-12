# pylint: disable=C0301
# flake8: noqa: E501
"""Advanced examples for resizing images using the iloveimg library and ResizeTask.

This script demonstrates advanced use cases for resizing image files
using the iLoveIMG API.

Examples include:
- Resizing a single image by pixels (width and height).
- Resizing a single image by percentage.
- Resizing multiple images in batch.
- Customizing advanced options: maintain aspect ratio, prevent enlarging small images.
- Setting custom output filenames for each resize operation.

Replace 'project_public_id' and 'project_secret_key' with your API credentials.
Update input file paths as needed.

Refer to the iLoveIMG API documentation for supported formats and advanced options.
"""

from iloveimg import ResizeTask

# Example 1: Resize a single image by pixels (width and height)
task_pixels = ResizeTask("project_public_id", "project_secret_key")
task_pixels.resize_mode = "pixels"
task_pixels.pixels_width = 800
task_pixels.pixels_height = 600
task_pixels.maintain_ratio = True  # Keep aspect ratio
task_pixels.no_enlarge_if_smaller = True  # Prevent enlarging small images
task_pixels.add_file("/path/to/input/image1.jpg")
task_pixels.set_output_filename("output_image_pixels.jpg")
task_pixels.execute()
task_pixels.download()

# Example 2: Resize a single image by percentage
task_percent = ResizeTask("project_public_id", "project_secret_key")
task_percent.resize_mode = "percentage"
task_percent.percentage = 50  # Resize to 50% of original size
task_percent.maintain_ratio = True
task_percent.no_enlarge_if_smaller = False  # Allow enlarging if smaller
task_percent.add_file("/path/to/input/image2.png")
task_percent.set_output_filename("output_image_percent.png")
task_percent.execute()
task_percent.download()

# Example 3: Batch resize multiple images by pixels
task_batch = ResizeTask("project_public_id", "project_secret_key")
task_batch.resize_mode = "pixels"
task_batch.pixels_width = 1024
task_batch.pixels_height = 768
task_batch.maintain_ratio = False  # Ignore aspect ratio
task_batch.no_enlarge_if_smaller = True
task_batch.add_file("/path/to/input/image3.jpg")
task_batch.add_file("/path/to/input/image4.png")
task_batch.add_file("/path/to/input/image5.bmp")
task_batch.set_output_filename(
    "output_batch_resized.zip"
)  # Output will be a zip if multiple files
task_batch.execute()
task_batch.download()
