"""This module demonstrates a basic example of how to use the iloveimg library
to resize a single image file using the ResizeTask class."""

from iloveimg import ResizeTask

my_task = ResizeTask()

file = my_task.add_file("tests/integration/files_samples/image_sample.jpg")

my_task.resize_mode = "pixels"
my_task.pixels_width = 800
my_task.pixels_height = 600
my_task.maintain_ratio = True
my_task.no_enlarge_if_smaller = True

my_task.execute()
my_task.set_output_filename("resize_basic.jpg")
my_task.download("output_live")
