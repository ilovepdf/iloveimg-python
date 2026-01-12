"""Integration tests for ConvertTask using the iLoveIMG API.

Covers:
- Full workflow: add image files, set conversion parameters, execute, and download
    results.
"""

from iloveimg import ConvertTask

from .base_task_integration_test import BaseTaskIntegrationTest


class TestConvertTaskIntegration(BaseTaskIntegrationTest):
    """
    Integration tests for ConvertTask using the iLoveIMG API.

    Covers:
    - Single file conversion to PNG, HEIC, and GIF formats.
    - Animated GIF conversion from multiple images with advanced parameters.
    - Full workflow: add image files, set parameters, execute, and download results.
    """

    task_class = ConvertTask

    def test_convert_single_file_png_to_jpg(self):
        """
        Test full flow: add PNG file, convert to JPG, execute, and download.
        """
        self.add_sample_file("image_sample.png")
        self.task.convert_to = "jpg"
        self.execute_task()
        self.download_result("image_sample_converted.jpg")

    def test_convert_single_file_jpg_to_png(self):
        """
        Test full flow: add JPG file, convert to PNG, execute, and download.
        """
        self.add_sample_file("image_sample.jpg")
        self.task.convert_to = "png"
        self.execute_task()
        self.download_result("image_sample_converted.png")

    def test_convert_single_file_jpg_to_gif(self):
        """
        Test full flow: add JPG file, convert to GIF, execute, and download.
        """
        self.add_sample_file("image_sample.jpg")
        self.task.convert_to = "gif"
        self.execute_task()
        self.download_result("image_sample_converted.gif")

    def test_convert_multiple_files_to_animated_gif(self):
        """
        Test the full flow: add multiple JPG files, convert to animated GIF,
        set advanced parameters, execute, and download.
        """
        # Add multiple sample image files for animation
        self.add_sample_file("animation-step-1.jpg")
        self.add_sample_file("animation-step-2.jpg")
        self.add_sample_file("animation-step-3.jpg")
        self.add_sample_file("animation-step-4.jpg")
        self.task.convert_to = "gif_animation"
        self.task.gif_time = 100  # 1 second per image (100 hundredths)
        self.task.gif_loop = True  # Loop forever
        self.execute_task()
        self.download_result("images_sample_animated.gif")

    def test_convert_multiple_files_to_animated_gif_no_loop(self):
        """
        Test full flow: add multiple JPG files, convert to animated GIF with no
        loop, execute, and download.
        """
        self.add_sample_file("animation-step-1.jpg")
        self.add_sample_file("animation-step-2.jpg")
        self.add_sample_file("animation-step-3.jpg")
        self.add_sample_file("animation-step-4.jpg")
        self.task.convert_to = "gif_animation"
        self.task.gif_time = 50  # 0.5 seconds per image
        self.task.gif_loop = False  # Play once, do not loop
        self.execute_task()
        self.download_result("images_sample_animated_once.gif")
