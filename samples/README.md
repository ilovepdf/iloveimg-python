# Samples

This directory contains example scripts demonstrating how to use the iLoveIMG Python library to interact with the iLoveIMG API.

Each script illustrates a specific task, such as compressing, resizing, converting, cropping images, and more. Examples are designed to be simple, self-contained, and easy to adapt for your own use cases.

---

## Structure

- Each script focuses on a single use case or workflow.
- Scripts are grouped by task type (compression, conversion, cropping, etc.).
- All scripts include a brief description and helpful comments at the top.
- Examples follow the project documentation and style guidelines.

---

## How to Run the Examples

Before running any example script:

1. **Set environment variables**
   Make sure you have set the required environment variables for authentication:
   - `ILOVEIMG_PUBLIC_KEY`
   - `ILOVEIMG_SECRET_KEY`
   - Optionally, `FOLDER_SAMPLE_PATH` for sample files

   You can copy `.docker/.env.sample` to `.docker/.env` and fill in your credentials.

2. **Install dependencies**
   Install the library and its dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```

3. **Run the script**
   Execute any example script with:
   ```bash
   python <script_name>.py
   ```

---

## List of Example Scripts

**Compression**
- `compress_basic.py`: Basic image compression example.
- `compress_intermediate.py`: Compress multiple images with custom parameters.
- `compress_advanced.py`: Advanced compression workflow.

**Conversion**
- `convert_basic.py`: Convert images between formats.
- `convert_advanced.py`: Advanced conversion, including animated GIFs and extra parameters.

**Cropping**
- `crop_basic.py`: Crop images using presets.
- `crop_intermediate.py`: Crop images with custom coordinates.

**Background Removal**
- `removebackground_basic.py`: Remove background from a single image.
- `removebackground_intermediate.py`: Remove background from multiple images.

**Resizing**
- `resize_basic.py`: Resize images by width, height, or percentage.
- `resize_advanced.py`: Advanced resizing scenarios.

**Rotation**
- `rotate_basic.py`: Rotate images by a specified angle.
- `rotate_intermediate.py`: Rotate multiple images with different angles.

**Upscaling**
- `upscale_basic.py`: Basic AI upscaling example.
- `upscale_intermediate.py`: Advanced upscaling workflow.

**Watermarking**
- `watermark_basic.py`: Add a simple watermark to an image.
- `watermark_advanced.py`: Advanced watermarking with custom options.

---

## More Information

- For full project documentation and API usage, see the [main README](../README.md).
- For detailed API reference, visit the [official iLoveIMG API docs](https://developer.iloveimg.com/docs).

---
