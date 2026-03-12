"""Sample script to demonstrate basic watermarking using the iLoveIMG library.

This example shows how to use the WatermarkTask class to add a simple text watermark
to a single image file.
"""

from iloveimg import WatermarkTask

my_task = WatermarkTask()

file = my_task.add_file("tests/integration/files_samples/image_sample.jpg")

watermark_element = my_task.add_element()
watermark_element.type = "text"
watermark_element.text = "Confidential"

my_task.execute()
my_task.set_output_filename("watermark_basic.jpg")
my_task.download("output_live")
