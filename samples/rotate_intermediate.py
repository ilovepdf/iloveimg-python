"""This module demonstrates an intermediate example of how to use the iloveimg library
to rotate multiple image files using the RotateTask class."""

from iloveimg import RotateTask

# To get your API key pair, visit: https://developer.iloveimg.com/user/projects
my_task = RotateTask("project_public_id", "project_secret_key")

# Add multiple image files with different rotation angles.
file1 = my_task.add_file("/path/to/file/image1.jpg")
file1.rotate = 90

# Rotation can also be set directly in the add_file call.
file2 = my_task.add_file("/path/to/file/image2.jpg", rotate=180)

# Execute the rotation for all added files.
my_task.execute()

# Set a custom output filename. Multiple files are delivered as a ZIP archive.
my_task.set_output_filename("rotate_intermediate.zip")

# Download the rotated images to the specified folder.
my_task.download("output_folder")
