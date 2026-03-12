"""Basic example of adding a text watermark to a single image file
using the WatermarkTask class."""

from iloveimg import WatermarkTask

# To get your API key pair, visit: https://developer.iloveimg.com/user/projects
my_task = WatermarkTask("project_public_id", "project_secret_key")

# Add the image file to watermark.
file = my_task.add_file("/path/to/file/image.jpg")

# Add a text watermark element.
watermark_element = my_task.add_element()
watermark_element.type = "text"
watermark_element.text = "Confidential"

# Execute the watermarking task.
my_task.execute()

# Set a custom output filename.
my_task.set_output_filename("watermark_basic.jpg")

# Download the watermarked image to the specified folder.
my_task.download("output_folder")
