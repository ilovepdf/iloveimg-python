"""Integration tests for UpScaleTask using the iLoveIMG API.

Covers:
- Full workflow: add image files, set parameters, execute, and download results.
- Includes edge cases and error handling.
"""

import pytest

from iloveimg import UpScaleTask

from .base_task_integration_test import BaseTaskIntegrationTest


@pytest.fixture
def upscale_task():
    """Fixture to initialize a UpScaleTask instance."""
    task = UpScaleTask()
    return task


class TestUpScaleTaskIntegration(BaseTaskIntegrationTest):
    """
    Integration tests for UpScaleTask using the iLoveIMG API.

    Covers:
    - Full workflow: add image files, set parameters, execute, and download results.
    - Includes edge cases and error handling.
    """

    task_class = UpScaleTask
    sample_file_path = "image_sample.jpg"

    def test_full_basic_h_flow(self):
        """
        Test the full flow: add a single file, set multiplier, execute, and download.
        """
        # Add sample image file to the task
        self.add_sample_file()

        # Set multiplier (required)
        self.task.multiplier = 2

        # Execute the task and check status
        self.execute_task()

        # Download the compressed file and verify
        self.download_result("image_basic_scaled.jpg")

    def test_full_advanced_upscale_flow(self):
        """
        Test the full flow: add a single file, set multiplier, execute, and download.
        """
        # Add multiple sample image files to the task
        self.add_sample_file()
        self.add_sample_file()

        # Set multiplier (required)
        self.task.multiplier = 4

        # Execute the task
        self.execute_task()

        # Download the scaled file and verify
        self.download_result("image_advanced_scaled.zip")
