"""Integration tests for file upload using the iLoveIMG API.

Covers:
- Full workflow: upload image files, execute task, and download results.
- Verifies that uploaded files receive a valid server_filename.
"""

from iloveimg import CompressTask

from .base_task_integration_test import BaseTaskIntegrationTest


class TestUploadFilesIntegration(BaseTaskIntegrationTest):
    """
    Integration tests for file upload using the iLoveIMG API.

    Covers:
    - Full upload workflow: add image file, verify server assignment, execute,
      and download results.
    """

    task_class = CompressTask

    def test_full_upload_flow(self):
        """Test the full upload flow."""

        # 1. Upload a IMG file and associate it with the task
        uploaded_file = self.add_sample_file()
        assert (
            getattr(uploaded_file, "server_filename", None) is not None
        ), "Uploaded file should have a server_filename."

        # 2. Execute the task and download the result
        self.execute_task()
        self.download_result("integration_image_compressed_sample.jpg")
