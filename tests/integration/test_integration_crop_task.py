"""Integration tests for CropTask using the iLoveIMG API.

Covers:
- Full workflow: add image files, set parameters, execute, and download results.
- Includes edge cases and error handling.
"""

import pytest

from iloveimg import CropTask

from .base_task_integration_test import BaseTaskIntegrationTest


@pytest.fixture
def crop_task():
    """Fixture to initialize a CropTask instance."""
    task = CropTask()
    return task


class TestCropTaskIntegration(BaseTaskIntegrationTest):
    """
    Integration tests for CropTask using the iLoveIMG API.

    Covers:
    - Full workflow: add image files, set parameters, execute, and download results.
    - Includes edge cases and error handling.
    """

    task_class = CropTask

    # def test_full_basic_crop_flow(self, crop_task):
    def test_full_basic_crop_flow(self):
        """
        Test the full flow: add a single file, set width, height, execute, and download.
        """
        # Add sample image file to the task
        self.add_sample_file()

        # Set width, height (required)
        self.task.width = 400
        self.task.height = 400

        # Execute the task and check status
        self.execute_task()

        # Download the compressed file and verify
        self.download_result("image_basic_cropped.jpg")

    def test_full_advanced_crop_flow(self):
        """
        Test the full flow: add a single file, set width, height, x, and y, execute,
        and download.
        """
        # Add sample image file to the task
        self.add_sample_file()

        # Set width, height (required)
        self.task.width = 400
        self.task.height = 400

        # Set x, y (optional)
        self.task.x = 300
        self.task.y = 300

        # Execute the task
        self.execute_task()

        # Download the cropped file and verify
        self.download_result("image_advanced_cropped.jpg")
