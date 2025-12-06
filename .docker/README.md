# Docker & Environment Setup

This directory contains Docker configuration files for developing and testing the **iLoveIMG Python** library in an isolated, reproducible environment.

---

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/) installed on your system.
- Environment variables configured as described below.

---

## Environment Variables

Before running Docker containers, you must set up the required environment variables:

1. Copy the sample environment file:

   ```bash
   cp .docker/.env.sample .docker/.env
   ```

2. Edit `.docker/.env` and set the following variables:

   - `ILOVEIMG_PUBLIC_KEY` – Your iLoveIMG project public key
   - `ILOVEIMG_SECRET_KEY` – Your iLoveIMG project secret key
   - `FOLDER_SAMPLE_PATH` – Path to sample files (default: `tests/integration/files_samples`)

**Note:**
The `.env` file is used by both local development and Docker containers. Never commit your real credentials.

---

## Quick Start

### 1. Build Docker Images

To build all Python version images (3.9–3.12):

```bash
docker-compose -f .docker/docker-compose.yml build
```

To build a specific Python version (e.g., Python 3.12):

```bash
docker-compose -f .docker/docker-compose.yml build python312
```

To force a rebuild (ignore cache):

```bash
docker-compose -f .docker/docker-compose.yml build --no-cache
```

### 2. Run Tests

To run all tests (unit and integration) in a specific Python version:

```bash
docker-compose -f .docker/docker-compose.yml run python39
```

For Python 3.10:

```bash
docker-compose -f .docker/docker-compose.yml run python310
```

Available services: `python39`, `python310`, `python311`, `python312`

#### Run Only Unit or Integration Tests

```bash
docker-compose -f .docker/docker-compose.yml run python39 pytest tests/unit
docker-compose -f .docker/docker-compose.yml run python39 pytest tests/integration
```

#### Run a Specific Test File

```bash
docker-compose -f .docker/docker-compose.yml run python39 pytest tests/unit/test_compress_task.py
```

---

## Development Workflow

- The project directory is mounted into the container as a volume.
- **Live code editing:** Changes to Python files are immediately reflected in the container.
- **No rebuilds needed:** Modify code and run tests without rebuilding the image.
- **Efficient iteration:** Quickly test changes across multiple Python versions.

Example workflow:

```bash
# Terminal 1: Run tests in Python 3.9
docker-compose -f .docker/docker-compose.yml run python39

# Terminal 2: Edit code in your IDE
# Changes are instantly available in the running container
```

---

## Using Direct Docker Commands

If you prefer to use Docker directly instead of Docker Compose:

```bash
# Build
docker build -t iloveimg-python39 -f .docker/Dockerfile .

# Run with environment file
docker run --env-file .docker/.env iloveimg-python39
```

---

## Troubleshooting

### Container exits after running tests

This is expected. The container runs tests and exits when complete.
To keep it running for debugging:

```bash
docker-compose -f .docker/docker-compose.yml run python39 bash
```

### Changes not reflected in container

- Ensure files are saved in your editor.
- Re-run tests (container picks up changes from mounted volume).

### Clear cache and rebuild

```bash
docker-compose -f .docker/docker-compose.yml down
docker-compose -f .docker/docker-compose.yml build --no-cache
```

---

## Reference

- Main project documentation: [../README.md](../README.md)
- Environment variable sample: [.env.sample](.env.sample)
- Official iLoveIMG API docs: [https://developer.iloveimg.com/docs](https://developer.iloveimg.com/docs)
