"""Intermediate example of upscaling multiple image files in a single batch
using the UpScaleTask class."""

from iloveimg import UpScaleTask

# To get your API key pair, visit: https://developer.iloveimg.com/user/projects
my_task = UpScaleTask("project_public_id", "project_secret_key")

# Set the upscaling multiplier. Allowed values: 2, 4.
my_task.multiplier = 4

# Add multiple image files to upscale in a single batch.
file1 = my_task.add_file("/path/to/file/image1.jpg")
file2 = my_task.add_file("/path/to/file/image2.jpg")
file3 = my_task.add_file("/path/to/file/image3.jpg")

# Execute the upscaling task for all added files.
my_task.execute()

# Set a custom output filename. Multiple files are delivered as a ZIP archive.
my_task.set_output_filename("upscale_intermediate.zip")

# Download the upscaled images to the specified folder.
my_task.download("output_folder")
