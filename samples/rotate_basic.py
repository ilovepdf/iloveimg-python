# pylint: disable=C0301
"""This module demonstrates a basic example of how to use the iloveimg library
to rotate a single image file using the RotateTask class.

The script shows how to rotate an image by a specified angle using the iLoveIMG API.
"""

from iloveimg import RotateTask

# You can call the task class directly
# To get your key pair, please visit https://developer.ilovepdf.com/user/projects
my_task = RotateTask("project_public_id", "project_secret_key")


# The 'file' variable keeps information about the server file ID and name.
# This information can be used later to manage or cancel the file if needed.
file = my_task.add_file("/path/to/file/image.jpg")

file.rotate = 90

# Optionally set a name for the output file.
my_task.set_output_filename("/path/to/output/image_output.jpg")

# Process files
my_task.execute()

# Download the file; if no path is set, it saves to the current folder.
my_task.download()
