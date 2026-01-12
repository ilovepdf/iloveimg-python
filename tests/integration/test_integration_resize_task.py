"""Integration tests for ResizeTask using the iLoveIMG API.

These tests validate the end-to-end behavior of resizing images:
  * Single file resizing by explicit pixel dimensions.
  * Single file resizing by percentage of original size.
  * Batch resizing of multiple input images.
  * Behavior of maintain_ratio and no_enlarge_if_smaller flags.

Each test executes the full workflow: append sample file(s), configure parameters,
execute the API task, wait for completion, and download the result.

The remote API credentials and sample file path are provided via environment
variables documented in .docker/.env.sample.
"""

from iloveimg import ResizeTask

from .base_task_integration_test import BaseTaskIntegrationTest


class TestResizeTaskIntegration(BaseTaskIntegrationTest):
    """
    Integration tests for ResizeTask.

    These tests cover:
      - Resizing a single image by pixel dimensions.
      - Resizing a single image by percentage of the original size.
      - Batch resizing multiple images in one task.
      - Advanced options: maintain_ratio and no_enlarge_if_smaller flags.

    Workflow per test:
      1. Append one or more sample image files.
      2. Configure resize parameters.
      3. Execute the remote task against the iLoveIMG API.
      4. Download and persist the resulting file(s).
    """

    task_class = ResizeTask

    def test_resize_single_file_by_pixels(self):
        """Resize a single image by pixel dimensions and download the result."""
        self.add_sample_file()
        self.task.resize_mode = "pixels"
        self.task.pixels_width = 800
        self.task.pixels_height = 600
        self.task.maintain_ratio = True
        self.task.no_enlarge_if_smaller = True
        self.execute_task()
        self.download_result("image_sample_resized_pixels.jpg")

    def test_resize_single_file_by_percentage(self):
        """
        Resize a single image by percentage of its original size and download the
        result.
        """
        self.add_sample_file()
        self.task.resize_mode = "percentage"
        self.task.percentage = 50  # 50% of original size
        self.task.maintain_ratio = True
        self.task.no_enlarge_if_smaller = False
        self.execute_task()
        self.download_result("image_sample_resized_percent.jpg")

    def test_resize_multiple_files_batch(self):
        """
        Resize multiple images in a batch using pixel dimensions and download as
        a zip archive.
        """
        self.add_sample_file()
        self.add_sample_file()
        self.task.resize_mode = "pixels"
        self.task.pixels_width = 1024
        self.task.pixels_height = 768
        self.task.maintain_ratio = False
        self.task.no_enlarge_if_smaller = True
        self.execute_task()
        self.download_result("images_sample_batch_resized.zip")

    def test_resize_with_no_enlarge_if_smaller_false(self):
        """
        Allow enlarging small images and verify the task completes
        and downloads correctly.
        """
        self.add_sample_file()
        self.task.resize_mode = "pixels"
        self.task.pixels_width = 1600
        self.task.pixels_height = 1200
        self.task.no_enlarge_if_smaller = False
        self.execute_task()
        self.download_result("image_sample_enlarged.jpg")
