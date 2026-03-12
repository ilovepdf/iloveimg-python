"""This module demonstrates a basic example of how to use the iloveimg library
to convert a single image file to another format using the ConvertTask class."""

from iloveimg import ConvertTask

# To get your API key pair, visit: https://developer.iloveimg.com/user/projects
my_task = ConvertTask("project_public_id", "project_secret_key")

# Add the image file to convert.
file = my_task.add_file("/path/to/file/image.jpg")

# Set the desired output format. Options: "jpg", "png", "gif", "gif_animation".
my_task.convert_to = "png"

# Execute the conversion.
my_task.execute()

# Set a custom output filename.
my_task.set_output_filename("convert_basic.png")

# Download the converted image to the specified folder.
my_task.download("output_folder")
