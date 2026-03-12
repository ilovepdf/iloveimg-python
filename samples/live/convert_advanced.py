"""Advanced examples for converting images using the iloveimg library and ConvertTask.

This script demonstrates advanced use cases for converting image files
to supported formats (JPG, PNG, GIF, animated GIF) using the iLoveIMG API.
"""

from iloveimg import ConvertTask

# Example 1: Convert a single PNG image to JPG format
my_task = ConvertTask()
my_task.convert_to = "jpg"
my_task.add_file("tests/integration/files_samples/image_sample.png")
my_task.execute()
my_task.set_output_filename("convert_advanced_png2jpg.jpg")
my_task.download("output_live")

# Example 2: Convert a single JPG image to PNG format
task_png = ConvertTask()
task_png.convert_to = "png"
task_png.add_file("tests/integration/files_samples/image_sample.jpg")
task_png.execute()
task_png.set_output_filename("convert_advanced_jpg2png.png")
task_png.download("output_live")

# Example 3: Convert a single JPG image to GIF format (static GIF)
task_gif = ConvertTask()
task_gif.convert_to = "gif"
task_gif.add_file("tests/integration/files_samples/image_sample.jpg")
task_gif.execute()
task_gif.set_output_filename("convert_advanced_jpg2gif.gif")
task_gif.download("output_live")

# Example 4: Convert multiple GIF images to animated GIF with advanced parameters
task_gif_anim = ConvertTask()
task_gif_anim.convert_to = "gif_animation"
task_gif_anim.add_file("tests/integration/files_samples/animation-step-1.jpg")
task_gif_anim.add_file("tests/integration/files_samples/animation-step-2.jpg")
task_gif_anim.add_file("tests/integration/files_samples/animation-step-3.jpg")
task_gif_anim.add_file("tests/integration/files_samples/animation-step-4.jpg")
task_gif_anim.gif_time = 100
task_gif_anim.gif_loop = True
task_gif_anim.execute()
task_gif_anim.set_output_filename("convert_advanced_animation.gif")
task_gif_anim.download("output_live")

# Example 5: Animated GIF that does NOT loop
task_gif_anim_once = ConvertTask()
task_gif_anim_once.convert_to = "gif_animation"
task_gif_anim_once.gif_time = 50
task_gif_anim_once.gif_loop = False
task_gif_anim_once.add_file("tests/integration/files_samples/animation-step-1.jpg")
task_gif_anim_once.add_file("tests/integration/files_samples/animation-step-2.jpg")
task_gif_anim_once.add_file("tests/integration/files_samples/animation-step-3.jpg")
task_gif_anim_once.add_file("tests/integration/files_samples/animation-step-4.jpg")
task_gif_anim_once.execute()
task_gif_anim_once.set_output_filename("convert_advanced_animation_no_loop.gif")
task_gif_anim_once.download("output_live")
