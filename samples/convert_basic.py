# pylint: disable=C0301
# flake8: noqa: E501
"""
This module demonstrates a basic example of how to use the iloveimg library
to convert a single image file to another format using the ConvertTask class.

The script shows how to convert an image (e.g., from PNG to JPG) using the iLoveIMG API.
"""

from iloveimg import ConvertTask

# You can call the task class directly
# To get your key pair, please visit https://developer.ilovepdf.com/user/projects
my_task = ConvertTask("project_public_id", "project_secret_key")

# The 'file' variable keeps information about the server file ID and name.
# This information can be used later to manage or cancel the file if needed.

file = my_task.add_file("/path/to/file/image.jpg")

# Set the desired output format (e.g., "jpg", "png", "gif", "gif_animation")
my_task.convert_to = "png"

# Optionally set a name for the output file.
my_task.set_output_filename("/path/to/output/image_converted.png")

# Process files
my_task.execute()

# And finally download the file. If no path is set, it will be downloaded in the current folder
my_task.download()
