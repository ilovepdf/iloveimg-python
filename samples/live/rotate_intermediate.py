"""This module demonstrates an intermediate example of how to use the iloveimg library
to rotate multiple image files with distinct angles using the RotateTask class."""

from iloveimg import RotateTask

my_task = RotateTask()

file1 = my_task.add_file("tests/integration/files_samples/image_sample.jpg")
file1.rotate = 90

file2 = my_task.add_file("tests/integration/files_samples/image_sample.jpg", rotate=180)

my_task.execute()
my_task.set_output_filename("rotate_intermediate.zip")
my_task.download("output_live")
