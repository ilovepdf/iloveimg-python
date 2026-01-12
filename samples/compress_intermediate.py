# pylint: disable=C0301
"""This module demonstrates an intermediate example of how to use the iloveimg library
to compress an image file using the CompressTask class. This example includes
authentication with public and secret keys."""

from iloveimg import CompressTask

# You can call the task class directly
# To get your key pair, please visit https://developer.ilovepdf.com/user/projects
my_task = CompressTask("project_public_id", "project_secret_key")

# file var keeps info about server file id, name...
# it can be used later to cancel file
file = my_task.add_file("/path/to/file/image.jpg")

# Set the compression level if needed. Options are: "low", "recommended", or "extreme".
# This step is optional.
my_task.compression_level = "extreme"

# Optionally set a name for the output file.
my_task.set_output_filename("/path/to/output/image_sample_output.jpg")

# Process files
my_task.execute()

# and finally download file. If no path is set, it will be downloaded in the current
# folder
my_task.download()
