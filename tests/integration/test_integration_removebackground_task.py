"""Integration tests for RemoveBackgroundTask using the iLoveIMG API.

Covers:
- Full workflow: add image files, execute background removal, and download results.
"""

from iloveimg import RemoveBackgroundTask

from .base_task_integration_test import BaseTaskIntegrationTest


class TestRemoveBackgroundTaskIntegration(BaseTaskIntegrationTest):
    """
    Integration tests for RemoveBackgroundTask using the iLoveIMG API.

    Covers:
    - Full workflow: add image files, execute background removal, and download results.
    """

    task_class = RemoveBackgroundTask

    def test_removebackground_single_file(self):
        """
        Test the full flow: add a single file, execute background removal,
        and download.
        """
        # Add sample image file to the task
        self.add_sample_file()

        # Execute the task and check status
        self.execute_task()

        # Download the background removed file and verify
        self.download_result("image_sample_background_removed.jpg")

    def test_removebackground_multiple_files(self):
        """
        Test the full flow: add multiple files, execute background removal,
        and download.
        """
        # Add multiple sample image files to the task for background removal
        self.add_sample_file()
        self.add_sample_file()

        # Execute the task and check status
        self.execute_task()

        # Download the background removed zip file and verify
        self.download_result("images_sample_background_removed.zip")
