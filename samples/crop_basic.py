"""This module demonstrates a basic example of how to use the iloveimg library
to crop a single image file using the CropTask class."""

from iloveimg import CropTask

# To get your API key pair, visit: https://developer.iloveimg.com/user/projects
my_task = CropTask("project_public_id", "project_secret_key")

# Add the image file to crop.
file = my_task.add_file("/path/to/file/image.jpg")

# Set crop dimensions in pixels.
my_task.width = 400
my_task.height = 300

# Execute the crop operation.
my_task.execute()

# Set a custom output filename.
my_task.set_output_filename("crop_basic.jpg")

# Download the cropped image to the specified folder.
my_task.download("output_folder")
