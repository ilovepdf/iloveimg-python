# pylint: disable=C0301
# flake8: noqa: E501
"""Advanced sample script for watermarking images using the iLoveIMG library.

This script demonstrates advanced watermarking features with the WatermarkTask class,
including multiple watermark elements, text and image watermarks, custom positioning,
font options, transparency, mosaic, and more.

Replace 'project_public_id' and 'project_secret_key' with your API credentials.
Update input file paths as needed.

Refer to the iLoveIMG API documentation for supported watermark options.

"""

from iloveimg import WatermarkTask

# Initialize the WatermarkTask with your API credentials.
task = WatermarkTask("project_public_id", "project_secret_key")

# Add an image file to watermark.
# file = task.add_file("/path/to/input/image.jpg")
file = task.add_file("image_sample.jpg")

# Example 1: Add a text watermark with advanced customization.
text_element = task.add_element()
text_element.type = "text"
text_element.text = "Confidential"
text_element.gravity = "SouthEast"
text_element.vertical_adjustment_percent = -10
text_element.horizontal_adjustment_percent = 10
text_element.rotation = 15
text_element.font_family = "Verdana"
text_element.font_style = "Bold"
text_element.font_size = 32
text_element.font_color = "#FF0000"
text_element.transparency = 80
text_element.mosaic = False

# Example 2: Add an image watermark with custom position and mosaic effect.
image_element = task.add_element()
image_element.type = "image"
# Set the watermark image by uploading it and linking its server filename.
# This requires the watermark image to be uploaded first.
file_element = image_element.set_image("/path/to/watermark/image.png")
image_element.gravity = "NorthWest"
image_element.x_pos_percent = 5
image_element.y_pos_percent = 5
image_element.width_percent = 20
image_element.height_percent = 20
image_element.transparency = 60
image_element.mosaic = True

# Set the output filename for the watermarked image.
task.set_output_filename("/path/to/output/image_output.png")

# Execute the watermarking task.
task.execute()

# Download the watermarked image.
task.download()
