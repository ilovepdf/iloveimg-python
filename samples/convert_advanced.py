"""Advanced examples for converting images using the iloveimg library and ConvertTask.

This script demonstrates advanced use cases for converting image files
to supported formats (JPG, PNG, GIF, animated GIF) using the iLoveIMG API.

Supported output formats and allowed input extensions:
    - jpg: png, gif, tif, psd, svg, webp, heic, raw
    - png: jpg
    - gif: jpg
    - gif_animation: gif
"""

from iloveimg import ConvertTask

# To get your API key pair, visit: https://developer.iloveimg.com/user/projects

# Example 1: Convert a single PNG image to JPG format.
my_task = ConvertTask("project_public_id", "project_secret_key")
my_task.convert_to = "jpg"
my_task.add_file("/path/to/input/image.png")
my_task.execute()
my_task.set_output_filename("convert_advanced_png2jpg.jpg")
my_task.download("output_folder")

# Example 2: Convert a single JPG image to PNG format.
task_png = ConvertTask("project_public_id", "project_secret_key")
task_png.convert_to = "png"
task_png.add_file("/path/to/input/image.jpg")
task_png.execute()
task_png.set_output_filename("convert_advanced_jpg2png.png")
task_png.download("output_folder")

# Example 3: Convert a single JPG image to static GIF format.
task_gif = ConvertTask("project_public_id", "project_secret_key")
task_gif.convert_to = "gif"
task_gif.add_file("/path/to/input/image.jpg")
task_gif.execute()
task_gif.set_output_filename("convert_advanced_jpg2gif.gif")
task_gif.download("output_folder")

# Example 4: Create an animated GIF from multiple images with loop.
task_gif_anim = ConvertTask("project_public_id", "project_secret_key")
task_gif_anim.convert_to = "gif_animation"
task_gif_anim.add_file("/path/to/input/image1.gif")
task_gif_anim.add_file("/path/to/input/image2.gif")
task_gif_anim.add_file("/path/to/input/image3.gif")
task_gif_anim.gif_time = 100  # Frame duration in hundredths of a second
task_gif_anim.gif_loop = True
task_gif_anim.execute()
task_gif_anim.set_output_filename("convert_advanced_animation.gif")
task_gif_anim.download("output_folder")

# Example 5: Create an animated GIF without loop.
task_gif_no_loop = ConvertTask("project_public_id", "project_secret_key")
task_gif_no_loop.convert_to = "gif_animation"
task_gif_no_loop.gif_loop = False
task_gif_no_loop.add_file("/path/to/input/image1.gif")
task_gif_no_loop.add_file("/path/to/input/image2.gif")
task_gif_no_loop.add_file("/path/to/input/image3.gif")
task_gif_no_loop.add_file("/path/to/input/image4.gif")
task_gif_no_loop.execute()
task_gif_no_loop.set_output_filename("convert_advanced_animation_no_loop.gif")
task_gif_no_loop.download("output_folder")
