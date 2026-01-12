# pylint: disable=C0301
"""This module demonstrates a basic example of how to use the iloveimg library
to compress a single image file using the CompressTask class."""


from iloveimg import CompressTask

# You can call the task class directly
# To get your key pair, please visit https://developer.ilovepdf.com/user/projects
my_task = CompressTask("project_public_id", "project_secret_key")

# The 'file' variable keeps information about the server file ID and name.
# This information can be used later to manage or cancel the file if needed.
file = my_task.add_file("/path/to/file/image.jpg")

# Process files
my_task.execute()

# and finally download file. If no path is set, it will be downloaded in the current
# folder
my_task.download()
