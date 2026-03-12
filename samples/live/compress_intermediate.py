"""This module demonstrates an intermediate example of how to use the iloveimg library
to compress an image file with the CompressTask class using environment-based credentials
and a custom compression level."""

from iloveimg import CompressTask

my_task = CompressTask()
file = my_task.add_file("tests/integration/files_samples/image_sample.jpg")
my_task.compression_level = "extreme"
my_task.execute()
my_task.set_output_filename("compress_intermediate.jpg")
my_task.download("output_live")
