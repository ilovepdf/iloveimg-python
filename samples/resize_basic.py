# pylint: disable=C0301
# flake8: noqa: E501
"""This module demonstrates a basic example of how to use the iloveimg library
to resize a single image file using the ResizeTask class."""

from iloveimg import ResizeTask

# You can call the task class directly
# To get your key pair, please visit https://developer.iloveimg.com/user/projects
my_task = ResizeTask("project_public_id", "project_secret_key")

# Add an image file to the resize task
file = my_task.add_file("/path/to/file/image.jpg")

# Set resize mode and dimensions
my_task.resize_mode = "pixels"  # or "percentage"
my_task.pixels_width = 800  # New width in pixels (required if mode is "pixels")
my_task.pixels_height = 600  # New height in pixels (required if mode is "pixels")
# If using percentage mode:
# my_task.resize_mode = "percentage"
# my_task.percentage = 50        # Resize to 50% of original size

# Optionally set whether to maintain aspect ratio and prevent enlarging small images
my_task.maintain_ratio = True
my_task.no_enlarge_if_smaller = True

# Optionally set a name for the output file.
my_task.set_output_filename("/path/to/output/image_output.jpg")


# Process files
my_task.execute()

# And finally download the file. If no path is set, it will be downloaded in the current folder
my_task.download()
