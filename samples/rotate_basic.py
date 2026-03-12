"""This module demonstrates a basic example of how to use the iloveimg library
to rotate a single image file using the RotateTask class."""

from iloveimg import RotateTask

# To get your API key pair, visit: https://developer.iloveimg.com/user/projects
my_task = RotateTask("project_public_id", "project_secret_key")

# Add the image file to rotate.
file = my_task.add_file("/path/to/file/image.jpg")

# Set the rotation angle. Allowed values: 0, 90, 180, 270.
file.rotate = 90

# Execute the rotation.
my_task.execute()

# Set a custom output filename.
my_task.set_output_filename("rotate_basic.jpg")

# Download the rotated image to the specified folder.
my_task.download("output_folder")
