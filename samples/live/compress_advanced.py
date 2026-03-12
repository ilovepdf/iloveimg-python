"""This module demonstrates an advanced example of using the iloveimg library.
It compresses multiple image files using the CompressTask class."""

from iloveimg import CompressTask

my_task = CompressTask()

file_1 = my_task.add_file("tests/integration/files_samples/animation-step-1.jpg")
file_2 = my_task.add_file("tests/integration/files_samples/animation-step-2.jpg")
file_3 = my_task.add_file("tests/integration/files_samples/animation-step-3.jpg")

my_task.compression_level = "extreme"

my_task.execute()
my_task.set_output_filename("compress_advanced.zip")
my_task.download("output_live")
