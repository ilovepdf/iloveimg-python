"""This module demonstrates a basic example of how to use the iloveimg library
to remove the background from a single image file using the RemoveBackgroundTask class.
"""

from iloveimg import RemoveBackgroundTask

my_task = RemoveBackgroundTask()
file = my_task.add_file("tests/integration/files_samples/image_sample.jpg")
my_task.execute()
my_task.set_output_filename("removebackground_basic.jpg")
my_task.download("output_live")
