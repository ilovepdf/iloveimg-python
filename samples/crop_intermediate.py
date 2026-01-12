# pylint: disable=C0301
# flake8: noqa: E501
"""This module demonstrates an intermediate example of how to use the iloveimg library
to crop a single image file using the CropTask class."""

from iloveimg import CropTask

# You can call the task class directly
# To get your key pair, please visit https://developer.ilovepdf.com/user/projects
my_task = CropTask("project_public_id", "project_secret_key")

# The 'file' variable keeps information about the server file ID and name.
# This information can be used later to manage or cancel the file if needed.
file = my_task.add_file("/path/to/file/image.jpg")

# Set crop dimensions and position
my_task.width = 500  # Width in pixels
my_task.height = 400  # Height in pixels
my_task.x = 50  # Horizontal starting point
my_task.y = 50  # Vertical starting point

# Optionally set a name for the output file.
my_task.set_output_filename("/path/to/output/image_output.jpg")


# Process files
my_task.execute()

# And finally download the file. If no path is set, it will be downloaded in the current folder
my_task.download()
