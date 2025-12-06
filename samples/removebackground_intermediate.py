# pylint: disable=C0301
# flake8: noqa: E501
"""This module demonstrates an intermediate example of how to use the iloveimg library
to remove the background from multiple image files using the RemoveBackgroundTask class.
"""

from iloveimg import RemoveBackgroundTask

# You can call the task class directly
# To get your key pair, please visit https://developer.ilovepdf.com/user/projects
my_task = RemoveBackgroundTask("project_public_id", "project_secret_key")

# Add multiple image files to the background removal task
file1 = my_task.add_file("/path/to/file/image1.jpg")
file2 = my_task.add_file("/path/to/file/image2.jpg")
file3 = my_task.add_file("/path/to/file/image3.jpg")

# Each 'file' variable contains information about the uploaded file on the server

# Set the output filename for the resulting ZIP archive
my_task.set_output_filename("/path/to/output/output.zip")

# Execute the background removal process for all added files
my_task.execute()

# And finally download the file. If no path is set, it will be downloaded in the current folder
my_task.download()
