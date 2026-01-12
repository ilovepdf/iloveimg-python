# pylint: disable=C0301
# flake8: noqa: E501
"""Sample script to demonstrate image upscaling for multiple files using the iLoveIMG library.

This example shows how to use the UpScaleTask class to upscale several image files in one batch.
"""

from iloveimg import UpScaleTask

# Instantiate the UpScaleTask class for image upscaling.
# To obtain your API key pair, visit: https://developer.iloveimg.com/user/projects
my_task = UpScaleTask()

# Set the upscaling multiplier (required).
# Allowed values: 2 (double resolution), 4 (quadruple resolution).
my_task.multiplier = 4

# Add multiple image files to upscale.
# Each returned 'file' object contains server file ID and name for further management.
file1 = my_task.add_file("/path/to/file/image1.jpg")
file2 = my_task.add_file("/path/to/file/image2.jpg")
file3 = my_task.add_file("/path/to/file/image3.jpg")


# Optionally, set the output filename for the upscaled images (as a zip archive).
my_task.set_output_filename("/path/to/output/output.zip")


# Execute the upscaling task.
my_task.execute()

# Download the upscaled images. If no path is specified, the zip file will be saved in the current directory.
my_task.download()
