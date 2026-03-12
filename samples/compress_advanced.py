"""This module demonstrates an advanced example of using the iloveimg library
to compress multiple image files using the CompressTask class."""

from iloveimg import CompressTask

# To get your API key pair, visit: https://developer.iloveimg.com/user/projects
my_task = CompressTask("project_public_id", "project_secret_key")

# Add multiple image files to compress in a single batch.
file_1 = my_task.add_file("/path/to/file/image_1.jpg")
file_2 = my_task.add_file("/path/to/file/image_2.jpg")
file_3 = my_task.add_file("/path/to/file/image_3.jpg")

# Set the compression level. Options: "low", "recommended", "extreme".
my_task.compression_level = "extreme"

# Execute the compression for all added files.
my_task.execute()

# Set a custom output filename. Multiple files are delivered as a ZIP archive.
my_task.set_output_filename("compress_advanced.zip")

# Download the compressed images to the specified folder.
my_task.download("output_folder")
