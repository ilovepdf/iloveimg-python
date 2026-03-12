"""This module demonstrates an intermediate example of how to use the iloveimg library
to remove the background from multiple image files using the RemoveBackgroundTask class.
"""

from iloveimg import RemoveBackgroundTask

my_task = RemoveBackgroundTask()

file1 = my_task.add_file("tests/integration/files_samples/image_sample.jpg")
file2 = my_task.add_file("tests/integration/files_samples/image_sample.jpg")
file3 = my_task.add_file("tests/integration/files_samples/image_sample.jpg")

my_task.execute()
my_task.set_output_filename("removebackground_intermediate.zip")
my_task.download("output_live")
