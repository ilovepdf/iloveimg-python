# pylint: disable=C0301
# flake8: noqa: E501
"""This module demonstrates a basic example of how to use the iloveimg library
to rotate multiple image files using the RotateTask class."""

from iloveimg import RotateTask

# You can call the task class directly
# To get your key pair, please visit https://developer.ilovepdf.com/user/projects
my_task = RotateTask("project_public_id", "project_secret_key")


# The 'file' variable keeps information about the server file ID and name.
# This information can be used later to manage or cancel the file if needed.
file1 = my_task.add_file("/path/to/file/image1.jpg")
file1.rotate = 90

file2 = my_task.add_file("/path/to/file/image2.jpg", rotate=180)

# Optionally set a name for the output file.
my_task.set_output_filename("/path/to/output/image_output.zip")


# Process files
my_task.execute()

# And finally download the file. If no path is set, it will be downloaded in the current folder
my_task.download()
