"""This module demonstrates a basic example of how to use the iloveimg library
to compress a single image file using the CompressTask class."""

from iloveimg import CompressTask

my_task = CompressTask()
file = my_task.add_file("tests/integration/files_samples/image_sample.jpg")
my_task.execute()
my_task.set_output_filename("compress_basic.jpg")
my_task.download("output_live")
