"""Sample script to demonstrate basic image upscaling using the iLoveIMG library.

This example shows how to use the UpScaleTask class to upscale a single image file.
"""

from iloveimg import UpScaleTask

my_task = UpScaleTask()
my_task.multiplier = 2
file = my_task.add_file("tests/integration/files_samples/image_sample.jpg")
my_task.execute()
my_task.set_output_filename("upscale_basic.jpg")
my_task.download("output_live")
