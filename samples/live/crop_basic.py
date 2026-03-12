"""This module demonstrates a basic example of how to use the iloveimg library
to crop a single image file using the CropTask class."""

from iloveimg import CropTask

my_task = CropTask()

file = my_task.add_file("tests/integration/files_samples/image_sample.jpg")

my_task.width = 400
my_task.height = 300

my_task.execute()
my_task.set_output_filename("crop_basic.jpg")
my_task.download("output_live")
