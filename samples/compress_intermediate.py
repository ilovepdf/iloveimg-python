"""This module demonstrates an intermediate example of how to use the iloveimg library
to compress an image file with a custom compression level using the CompressTask class.
"""

from iloveimg import CompressTask

# To get your API key pair, visit: https://developer.iloveimg.com/user/projects
my_task = CompressTask("project_public_id", "project_secret_key")

# Add the image file to compress.
file = my_task.add_file("/path/to/file/image.jpg")

# Set the compression level. Options: "low", "recommended", "extreme".
my_task.compression_level = "extreme"

# Execute the compression.
my_task.execute()

# Set a custom output filename.
my_task.set_output_filename("compress_intermediate.jpg")

# Download the compressed image to the specified folder.
my_task.download("output_folder")
