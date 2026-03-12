"""This module demonstrates an intermediate example of how to use the iloveimg library
to crop a single image file using the CropTask class with custom positional offsets."""

from iloveimg import CropTask

my_task = CropTask()

file = my_task.add_file("tests/integration/files_samples/image_sample.jpg")

my_task.width = 500
my_task.height = 400
my_task.x = 50
my_task.y = 50

my_task.execute()
my_task.set_output_filename("crop_intermediate.jpg")
my_task.download("output_live")
