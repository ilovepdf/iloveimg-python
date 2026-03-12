"""Advanced sample script for watermarking images using the iLoveIMG library.

This script demonstrates advanced watermarking features with the WatermarkTask class,
including multiple watermark elements, text and image watermarks, custom positioning,
font options, transparency, mosaic, and more.
"""

from iloveimg import WatermarkTask

task = WatermarkTask()

file = task.add_file("tests/integration/files_samples/image_sample.jpg")

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
file_element = image_element.set_image(
    "tests/integration/files_samples/logo_iloveimg.jpg"
)
image_element.gravity = "NorthWest"
image_element.x_pos_percent = 5
image_element.y_pos_percent = 5
image_element.width_percent = 20
image_element.height_percent = 20
image_element.transparency = 60
image_element.mosaic = True

task.execute()
task.set_output_filename("watermark_advanced.png")
task.download("output_live")
