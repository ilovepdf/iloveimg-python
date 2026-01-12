# pylint: disable=C0301
# flake8: noqa: E501

"""
Advanced examples for converting images using the iloveimg library and ConvertTask.

This script demonstrates advanced use cases for converting image files
to supported formats (JPG, PNG, GIF, animated GIF) using the iLoveIMG API.

Examples include:
- Converting a single image to PNG or static GIF formats.
- Creating animated GIFs from GIF images, with configurable frame duration and loop settings.
- Setting custom output filenames for each conversion.

Replace 'project_public_id' and 'project_secret_key' with your API credentials.
Update input file paths as needed.

Supported output formats and allowed input extensions:
    - jpg: png, gif, tif, psd, svg, webp, heic, raw
    - png: jpg
    - gif: jpg
    - gif_animation: gif

Refer to the iLoveIMG API documentation for supported formats and advanced options.
"""

from iloveimg import ConvertTask

# You can call the task class directly
# To get your key pair, please visit https://developer.ilovepdf.com/user/projects

# Example 1: Convert a single PNG image to JPG format
task_jpg = ConvertTask("project_public_id", "project_secret_key")
task_jpg.convert_to = "jpg"
task_jpg.add_file(
    "/path/to/input/image.png"
)  # Allowed: png, gif, tif, psd, svg, webp, heic, raw
task_jpg.set_output_filename("output_image.jpg")
task_jpg.execute()
task_jpg.download()

# Example 2: Convert a single JPG image to PNG format
task_png = ConvertTask("project_public_id", "project_secret_key")
task_png.convert_to = "png"
task_png.add_file("/path/to/input/image.jpg")  # Allowed: jpg
task_png.set_output_filename("output_image.png")
task_png.execute()
task_png.download()

# Example 3: Convert a single JPG image to GIF format (static GIF)
task_gif = ConvertTask("project_public_id", "project_secret_key")
task_gif.convert_to = "gif"
task_gif.add_file("/path/to/input/image.jpg")  # Allowed: jpg
task_gif.set_output_filename("output_image.gif")
task_gif.execute()
task_gif.download()

# Example 4: Convert multiple GIF images to animated GIF with advanced parameters
task_gif_anim = ConvertTask("project_public_id", "project_secret_key")
task_gif_anim.convert_to = "gif_animation"
# Add multiple GIF images for animation (only GIF allowed)
task_gif_anim.add_file("/path/to/input/image1.gif")
task_gif_anim.add_file("/path/to/input/image2.gif")
task_gif_anim.add_file("/path/to/input/image3.gif")
task_gif_anim.gif_time = 100  # 1 second per image (100 hundredths)
task_gif_anim.gif_loop = True  # Loop forever
task_gif_anim.set_output_filename("output_animation.gif")
task_gif_anim.execute()
task_gif_anim.download()

# Example 5: Animated GIF that does NOT loop
task_gif_anim_once = ConvertTask("project_public_id", "project_secret_key")
task_gif_anim_once.convert_to = "gif_animation"
task_gif_anim_once.add_file("/path/to/input/image1.gif")
task_gif_anim_once.add_file("/path/to/input/image2.gif")
task_gif_anim_once.gif_time = 50  # 0.5 seconds per image
task_gif_anim_once.gif_loop = False  # Play once, do not loop
task_gif_anim_once.set_output_filename("output_animation_once.gif")
task_gif_anim_once.execute()
task_gif_anim_once.download()
