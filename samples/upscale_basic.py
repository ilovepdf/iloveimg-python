"""Basic example of upscaling a single image file using the UpScaleTask class.

This script shows how to upscale an image to double its resolution using the iLoveIMG API.
"""

from iloveimg import UpScaleTask

# To get your API key pair, visit: https://developer.iloveimg.com/user/projects
my_task = UpScaleTask("project_public_id", "project_secret_key")

# Set the upscaling multiplier. Allowed values: 2, 4.
my_task.multiplier = 2

# Add the image file to upscale.
file = my_task.add_file("/path/to/file/image.jpg")

# Execute the upscaling task.
my_task.execute()

# Set a custom output filename.
my_task.set_output_filename("upscale_basic.jpg")

# Download the upscaled image to the specified folder.
my_task.download("output_folder")
