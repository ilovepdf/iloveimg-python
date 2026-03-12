"""This module demonstrates an intermediate example of how to use the iloveimg library
to remove the background from multiple image files using the RemoveBackgroundTask class.
"""

from iloveimg import RemoveBackgroundTask

# To get your API key pair, visit: https://developer.iloveimg.com/user/projects
my_task = RemoveBackgroundTask("project_public_id", "project_secret_key")

# Add multiple image files for background removal.
file1 = my_task.add_file("/path/to/file/image1.jpg")
file2 = my_task.add_file("/path/to/file/image2.jpg")
file3 = my_task.add_file("/path/to/file/image3.jpg")

# Execute the background removal for all added files.
my_task.execute()

# Set a custom output filename. Multiple files are delivered as a ZIP archive.
my_task.set_output_filename("removebackground_intermediate.zip")

# Download the processed images to the specified folder.
my_task.download("output_folder")
