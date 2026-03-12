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

## Installation

You can install the library via [PIP](https://pypi.org/project/pip/). Run the following command:

```bash
pip install iloveimg
```

For other install options (source, pre-release), see [INSTALL.md](INSTALL.md).

## Quick Start

1. Get your API keys from [https://developer.iloveimg.com](https://developer.iloveimg.com)
2. Run a task:

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
- Installation: [`INSTALL.md`](INSTALL.md) - All install options
- Development: [`DEVELOPMENT.md`](DEVELOPMENT.md) - Contributing & setup
- Docker & environment setup: [`.docker/`](.docker/README.md)

For full API docs, visit [developer.iloveimg.com](https://developer.iloveimg.com/docs)
