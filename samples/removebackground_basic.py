# pylint: disable=C0301
# flake8: noqa: E501
"""This module demonstrates a basic example of how to use the iloveimg library
to remove the background from a single image file using the RemoveBackgroundTask class.
"""

from iloveimg import RemoveBackgroundTask

# You can call the task class directly
# To get your key pair, please visit https://developer.ilovepdf.com/user/projects
my_task = RemoveBackgroundTask("project_public_id", "project_secret_key")


# Add a single image file to the background removal task
file = my_task.add_file("/path/to/file/image.jpg")

# The 'file' variable contains information about the uploaded file on the server

# Set the output filename for the processed image
my_task.set_output_filename("/path/to/output/image.jpg")

# Execute the background removal process
my_task.execute()

# Download the resulting image file; if no path is set, it will be saved in the current folder
my_task.download()
