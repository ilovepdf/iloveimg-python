"""Basic example of converting a single image file to another format
using the ConvertTask class."""

from iloveimg import ConvertTask

my_task = ConvertTask()
file = my_task.add_file("tests/integration/files_samples/image_sample.jpg")
my_task.convert_to = "png"
my_task.execute()
my_task.set_output_filename("convert_basic.png")
my_task.download("output_live")
