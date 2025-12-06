# pylint: disable=C0301
"""This module demonstrates an advanced example of using the iloveimg library.
It compresses multiple image files using the CompressTask class."""


from iloveimg import CompressTask

# You can call the task class directly
# To get your key pair, please visit https://developer.ilovepdf.com/user/projects
my_task = CompressTask("project_public_id", "project_secret_key")

# Each file variable keeps information about the server file ID, name, etc.
# These variables can be used later for operations like canceling the file.
file_1 = my_task.add_file("/path/to/file/image_1.jpg")
file_2 = my_task.add_file("/path/to/file/image_2.jpg")
file_3 = my_task.add_file("/path/to/file/image_3.jpg")

# Set the compression level if needed. Options are: "low", "recommended", or "extreme".
# This step is optional.
my_task.compression_level = "extreme"

# Optionally set a name for the output file.
# In this example, the output will be a ZIP file containing all compressed images.
my_task.set_output_filename("/path/to/output/image_sample_output.zip")

# Process files
my_task.execute()

# and finally download file. If no path is set, it will be downloaded in the current
# folder
my_task.download()
