"""Advanced examples for resizing images using the iloveimg library and ResizeTask.

This script demonstrates advanced use cases for resizing image files
using the iLoveIMG API.

Examples include:
- Resizing a single image by pixels (width and height).
- Resizing a single image by percentage.
- Resizing multiple images in batch.
- Customizing advanced options: maintain aspect ratio, prevent enlarging small images.
- Setting custom output filenames for each resize operation.
"""

from iloveimg import ResizeTask

# Example 1: Resize a single image by pixels (width and height)
task_pixels = ResizeTask()
task_pixels.resize_mode = "pixels"
task_pixels.pixels_width = 800
task_pixels.pixels_height = 600
task_pixels.maintain_ratio = True
task_pixels.no_enlarge_if_smaller = True
task_pixels.add_file("tests/integration/files_samples/image_sample.jpg")
task_pixels.execute()
task_pixels.set_output_filename("resize_advanced_pixels.jpg")
task_pixels.download("output_live")

# Example 2: Resize a single image by percentage
task_percent = ResizeTask()
task_percent.resize_mode = "percentage"
task_percent.percentage = 50
task_percent.maintain_ratio = True
task_percent.no_enlarge_if_smaller = False
task_percent.add_file("tests/integration/files_samples/image_sample.png")
task_percent.execute()
task_percent.set_output_filename("resize_advanced_percentage.png")
task_percent.download("output_live")

# Example 3: Batch resize multiple images by pixels
task_batch = ResizeTask()
task_batch.resize_mode = "pixels"
task_batch.pixels_width = 1024
task_batch.pixels_height = 768
task_batch.maintain_ratio = False
task_batch.no_enlarge_if_smaller = True
task_batch.add_file("tests/integration/files_samples/image_sample.jpg")
task_batch.add_file("tests/integration/files_samples/image_sample.jpg")
task_batch.add_file("tests/integration/files_samples/image_sample.jpg")
task_batch.execute()
task_batch.set_output_filename("resize_advanced_batch.zip")
task_batch.download("output_live")
