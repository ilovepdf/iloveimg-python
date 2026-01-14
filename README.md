# iLoveIMG API - Python Library

[![PyPI version](https://img.shields.io/pypi/v/iloveimg.svg)](https://pypi.org/project/iloveimg/)
[![Python versions](https://img.shields.io/pypi/pyversions/iloveimg.svg)](https://pypi.org/project/iloveimg/)
[![License](https://img.shields.io/pypi/l/iloveimg.svg)](https://pypi.org/project/iloveimg/)

A Python library for [iLoveIMG API](https://developer.iloveimg.com) to automate image processing tasks such as compressing, resizing, converting, cropping, watermarking, removing backgrounds, and more.

You can sign up for an iLoveIMG account at https://developer.iloveimg.com

Develop and automate image processing tasks like Compress, Convert, Crop, Resize, Rotate, Watermark, Remove Background, and Upscale. Each task supports several settings to get your desired results.

---

## Requirements

- Python 3.10 to 3.14

---

## Installation

Install from PyPI:

```bash
pip install iloveimg
```

Or install the latest version from source:

```bash
pip install -U git+https://github.com/ilovepdf/iloveimg-python.git@main#egg=iloveimg
```

---

## Getting Started

Simple usage looks like:

```python
from iloveimg import CompressTask

task = CompressTask(public_key="your_public_key", secret_key="your_secret_key")
task.add_file("input.jpg")
task.execute()
task.download("output_folder")
```

---

## Project Structure & Documentation

- Core library: [`iloveimg/`](iloveimg/README.md)
- Example scripts: [`samples/`](samples/README.md)
- Unit & integration tests: [`tests/`](tests/README.md)
- Docker & environment setup: [`.docker/`](.docker/README.md)

For detailed API documentation, visit the [official iLoveIMG API docs](https://developer.iloveimg.com/docs).

---
