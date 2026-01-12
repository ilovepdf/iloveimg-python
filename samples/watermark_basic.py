# pylint: disable=C0301
# flake8: noqa: E501
"""Sample script to demonstrate basic watermarking using the iLoveIMG library.

This example shows how to use the WatermarkTask class to add a simple text watermark
to a single image file.
"""

from iloveimg import WatermarkTask

# Instantiate the WatermarkTask class for watermarking images.
# To obtain your API key pair, visit: https://developer.iloveimg.com/user/projects
my_task = WatermarkTask("project_public_id", "project_secret_key")

# Add an image file to watermark.
# The returned 'file' object is a WatermarkFile instance for further configuration.
file = my_task.add_file("/path/to/file/image.jpg")

# Add a watermark element.
watermark_element = my_task.add_element()

# Set watermark type to text and provide the watermark text.
watermark_element.type = "text"
watermark_element.text = "Confidential"

# Optionally, set the output filename for the watermarked image.
my_task.set_output_filename("/path/to/output/image.jpg")

# Execute the watermarking task.
my_task.execute()

# Download the watermarked image. If no path is specified, it will be saved in the current directory.
my_task.download()
