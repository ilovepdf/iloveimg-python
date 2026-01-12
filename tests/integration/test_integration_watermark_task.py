"""Integration tests for WatermarkTask using the iLoveIMG API.

This module verifies the integration of watermarking functionality, covering:
- Full workflow: adding image files, configuring watermark elements, executing the task,
    and downloading results.
- Scenarios for both text and image watermarks.
- Batch processing of multiple files with a watermark.
"""

from iloveimg import WatermarkTask

from .base_task_integration_test import BaseTaskIntegrationTest


class TestWatermarkTaskIntegration(BaseTaskIntegrationTest):
    """
    Integration tests for WatermarkTask using the iLoveIMG API.

    This class covers:
    - Watermarking a single image with a text watermark.
    - Watermarking a single image with an image watermark.
    - Watermarking multiple images in batch with a text watermark.
    - The complete workflow: file upload, watermark configuration, task execution, and
        result download.
    """

    task_class = WatermarkTask

    def test_watermark_single_file_with_text(self):
        """
        Test watermarking a single image file with a text watermark.

        Steps:
        - Add a sample image file to the task.
        - Add a text watermark element with specific properties (text, font size,
            gravity, opacity).
        - Execute the watermark task.
        - Download the resulting watermarked image.
        """
        self.add_sample_file()
        # Add a watermark element (text)
        watermark_element = self.task.add_element()
        watermark_element.type = "text"
        watermark_element.text = "Confidential"
        watermark_element.font_size = 32
        watermark_element.gravity = "SouthEast"
        watermark_element.opacity = 0.7
        output_filename = "image_sample_watermarked_text.jpg"
        self.execute_task()
        self.download_result(output_filename)

    def test_watermark_single_file_with_image(self):
        """
        Test watermarking a single image file with an image watermark.

        Steps:
        - Add a sample image file to the task.
        - Add an image watermark element, set its image and properties
          (gravity, opacity, position, size, transparency, mosaic).
        - Execute the watermark task.
        - Download the resulting watermarked image.
        """
        self.add_sample_file()
        # Add a watermark element (image)
        watermark_element = self.task.add_element()
        watermark_element.type = "image"
        watermark_image_path = self.resolve_sample_file_path("logo_iloveimg.jpg")
        watermark_element.set_image(watermark_image_path)
        watermark_element.gravity = "NorthWest"
        watermark_element.opacity = 0.5
        watermark_element.x_pos_percent = 5
        watermark_element.y_pos_percent = 5
        watermark_element.width_percent = 20
        watermark_element.height_percent = 20
        watermark_element.transparency = 60
        watermark_element.mosaic = True
        output_filename = "image_sample_watermarked_logo.jpg"
        self.execute_task()
        self.download_result(output_filename)

    def test_watermark_multiple_files_with_text(self):
        """
        Test watermarking multiple image files with the same text watermark.

        Steps:
        - Add multiple sample image files to the task.
        - Add a text watermark element with specific properties (text, font size,
            gravity, opacity).
        - Execute the watermark task.
        - Download the resulting batch of watermarked images as a ZIP file.
        """
        self.add_sample_file()
        self.add_sample_file("logo_iloveimg.jpg")
        watermark_element = self.task.add_element()
        watermark_element.type = "text"
        watermark_element.text = "Sample Batch"
        watermark_element.font_size = 24
        watermark_element.gravity = "Center"
        watermark_element.opacity = 0.6
        self.execute_task()
        self.download_result("batch_watermarked_text.zip")
