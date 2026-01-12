# Integration Tests

This folder contains integration tests for the iLoveIMG Python library. Integration tests are designed to verify the correct interaction between the library and the iLoveIMG API, as well as to validate end-to-end workflows involving real API calls and file operations.

## Structure

- Each test file targets a specific feature or workflow (e.g., image compression, resizing, conversion).
- Tests may require valid API credentials and sample image files.

## Running Integration Tests

1. Ensure you have a valid `.env` file in the `.docker/` directory with the following variables set:
   - `ILOVEIMG_PUBLIC_KEY`
   - `ILOVEIMG_SECRET_KEY`
   - `FOLDER_SAMPLE_PATH` (default: `tests/integration/files_samples`)

2. Run the tests using your preferred test runner (e.g., `pytest`).

## Test Files

| File Name                                   | Description                                                                                  |
|---------------------------------------------|----------------------------------------------------------------------------------------------|
| test_integration_00_auth.py                 | Integration tests for authentication and API key validation.                                 |
| test_integration_01_upload_files.py         | Integration tests for uploading files to the API.                                            |
| test_integration_compress_task.py           | Integration tests for CompressTask, covering full workflow: adding files, setting compression parameters, executing, and downloading results. |
| test_integration_convert_task.py            | Integration tests for ConvertTask, covering format conversion, advanced options, and downloads. |
| test_integration_crop_task.py               | Integration tests for CropTask, covering full workflow: adding files, setting crop parameters, executing, and downloading results, including edge cases and error handling. |
| test_integration_removebackground_task.py   | Integration tests for RemoveBackgroundTask, verifying background removal via the iLoveIMG API.|
| test_integration_resize_task.py             | Integration tests for ResizeTask, covering resizing by dimensions and percentage.            |
| test_integration_rotate_task.py             | Integration tests for RotateTask, verifying image rotation via the iLoveIMG API.             |
| test_integration_upscale_task.py            | Integration tests for UpscaleTask, verifying AI-based upscaling and result download.         |
| test_integration_watermark_task.py          | Integration tests for WatermarkTask, covering text and image watermarking workflows.         |

Update this table as new integration tests are added.

## Notes

- Integration tests may consume API quota and require internet access.
- Sensitive data such as API keys should never be committed to the repository.
