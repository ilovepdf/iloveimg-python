"""Sample script to demonstrate image upscaling for multiple files using the iLoveIMG library.

This example shows how to use the UpScaleTask class to upscale several image files in one batch.
"""

from iloveimg import UpScaleTask

my_task = UpScaleTask()
my_task.multiplier = 4

file1 = my_task.add_file("tests/integration/files_samples/animation-step-1.jpg")
file2 = my_task.add_file("tests/integration/files_samples/animation-step-2.jpg")
file3 = my_task.add_file("tests/integration/files_samples/animation-step-3.jpg")

my_task.execute()
my_task.set_output_filename("upscale_intermediate.zip")
my_task.download("output_live")
