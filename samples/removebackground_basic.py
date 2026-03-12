"""This module demonstrates a basic example of how to use the iloveimg library
to remove the background from a single image file using the RemoveBackgroundTask class.
"""

from iloveimg import RemoveBackgroundTask

# To get your API key pair, visit: https://developer.iloveimg.com/user/projects
my_task = RemoveBackgroundTask("project_public_id", "project_secret_key")

# Add the image file for background removal.
file = my_task.add_file("/path/to/file/image.jpg")

# Execute the background removal.
my_task.execute()

# Set a custom output filename.
my_task.set_output_filename("removebackground_basic.jpg")

# Download the processed image to the specified folder.
my_task.download("output_folder")
