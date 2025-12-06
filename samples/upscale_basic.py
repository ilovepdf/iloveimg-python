# pylint: disable=C0301
# flake8: noqa: E501
"""Sample script to demonstrate basic image upscaling using the iLoveIMG library.

This example shows how to use the UpScaleTask class to upscale a single image file.
"""

from iloveimg import UpScaleTask

# Instantiate the UpScaleTask class for image upscaling.
# To obtain your API key pair, visit: https://developer.iloveimg.com/user/projects
my_task = UpScaleTask()

# Set the upscaling multiplier (required).
# Allowed values: 2 (double resolution), 4 (quadruple resolution).
my_task.multiplier = 2

# Add an image file to upscale.
# The returned 'file' object contains server file ID and name for further management.
file = my_task.add_file("/path/to/file/imagejpg")

# Optionally, set the output filename for the upscaled image.
my_task.set_output_filename("/path/to/output/image_output.jpg")


# Execute the upscaling task.
my_task.execute()

# Download the upscaled image. If no path is specified, it will be saved in the current directory.
my_task.download()
