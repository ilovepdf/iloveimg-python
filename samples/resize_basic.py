"""This module demonstrates a basic example of how to use the iloveimg library
to resize a single image file using the ResizeTask class."""

from iloveimg import ResizeTask

# To get your API key pair, visit: https://developer.iloveimg.com/user/projects
my_task = ResizeTask("project_public_id", "project_secret_key")

# Add the image file to resize.
file = my_task.add_file("/path/to/file/image.jpg")

# Set resize mode to pixels and define target dimensions.
my_task.resize_mode = "pixels"
my_task.pixels_width = 800
my_task.pixels_height = 600

# Maintain the original aspect ratio and prevent enlarging small images.
my_task.maintain_ratio = True
my_task.no_enlarge_if_smaller = True

# Execute the resize operation.
my_task.execute()

# Set a custom output filename.
my_task.set_output_filename("resize_basic.jpg")

# Download the resized image to the specified folder.
my_task.download("output_folder")
