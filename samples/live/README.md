# Live Sample Scripts

This directory contains **runnable example scripts** that execute real API calls against the iLoveIMG API. Each script mirrors a corresponding template in the parent [`samples/`](../README.md) directory, but is configured to run immediately using environment variables for authentication and real sample files from the test fixtures.

---

## Differences from `samples/`

| Aspect | `samples/` | `samples/live/` |
|---|---|---|
| API credentials | Placeholder strings (`"project_public_id"`) | Read from environment variables |
| File paths | Placeholder paths (`/path/to/file/image.jpg`) | Real paths (`tests/integration/files_samples/...`) |
| Purpose | Documentation and reference | Direct execution against the API |
| Output | N/A | Downloaded to `output_live/` |

---

## Prerequisites

1. **Set environment variables** for API authentication:
   - `ILOVEIMG_PUBLIC_KEY`
   - `ILOVEIMG_SECRET_KEY`

   You can copy `.env.example` to `.env` and fill in your credentials. See [`.docker/README.md`](../../.docker/README.md) for details.

2. **Ensure sample files exist** in `tests/integration/files_samples/`. The following files are used across scripts:
   - `image_sample.jpg`
   - `image_sample.png`
   - `logo_iloveimg.jpg`
   - `animation-step-1.jpg`, `animation-step-2.jpg`, `animation-step-3.jpg`, `animation-step-4.jpg`

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run

From the project root directory:

```bash
python samples/live/<script_name>.py
```

Output files are saved to the `output_live/` directory relative to where the script is executed.

---

## List of Live Example Scripts

### Compression

| Script | Description |
|---|---|
| `compress_basic.py` | Compress a single image with default settings. |
| `compress_intermediate.py` | Compress a single image with a custom compression level. |
| `compress_advanced.py` | Compress multiple images with extreme compression. |

### Conversion

| Script | Description |
|---|---|
| `convert_basic.py` | Convert a single image to another format (e.g., JPG to PNG). |
| `convert_advanced.py` | Convert multiple images to animated GIF with advanced parameters. |

### Cropping

| Script | Description |
|---|---|
| `crop_basic.py` | Crop a single image with specified width and height. |
| `crop_intermediate.py` | Crop a single image with custom coordinates (x, y offset). |

### Background Removal

| Script | Description |
|---|---|
| `removebackground_basic.py` | Remove the background from a single image. |
| `removebackground_intermediate.py` | Remove the background from multiple images. |

### Resizing

| Script | Description |
|---|---|
| `resize_basic.py` | Resize a single image by pixel dimensions. |
| `resize_advanced.py` | Resize with percentage mode and advanced options. |

### Rotation

| Script | Description |
|---|---|
| `rotate_basic.py` | Rotate a single image by a specified angle. |
| `rotate_intermediate.py` | Rotate multiple images with different angles. |

### Upscaling

| Script | Description |
|---|---|
| `upscale_basic.py` | Upscale a single image using AI with 2x multiplier. |
| `upscale_intermediate.py` | Upscale multiple images with 4x multiplier. |

### Watermarking

| Script | Description |
|---|---|
| `watermark_basic.py` | Add a simple text watermark to a single image. |
| `watermark_advanced.py` | Add multiple watermark elements (text and image) with advanced customization. |

---

## More Information

- For template examples with detailed inline comments, see the parent [`samples/`](../README.md) directory.
- For full project documentation, see the [main README](../../README.md).
- For API reference, visit the [official iLoveIMG API docs](https://developer.iloveimg.com/docs).
