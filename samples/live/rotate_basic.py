"""This module demonstrates a basic example of how to use the iloveimg library
to rotate a single image file using the RotateTask class.

The script shows how to rotate an image by a specified angle using the iLoveIMG API.
"""

from iloveimg import RotateTask

my_task = RotateTask()

file = my_task.add_file("tests/integration/files_samples/image_sample.jpg")
file.rotate = 90

my_task.execute()
my_task.set_output_filename("rotate_basic.jpg")
my_task.download("output_live")
