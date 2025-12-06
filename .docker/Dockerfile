ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION}-slim

# Create non-root user for security
RUN adduser --disabled-password --gecos '' appuser

# Set working directory
WORKDIR /src

# Copy project configuration files first (rarely change)
COPY pyproject.toml setup.cfg ./
COPY requirements.txt requirements_dev.txt requirements_test.txt ./

# Install dependencies as root before switching to appuser
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements_test.txt

# Copy source code and tests
COPY iloveimg ./iloveimg
COPY tests ./tests
COPY pytest.ini ./

# Change ownership to appuser
RUN chown -R appuser:appuser /src

USER appuser

# Set Python environment variables
ENV PYTHONPATH=/src
ENV PYTHONUNBUFFERED=1
ENV PATH="/home/appuser/.local/bin:$PATH"

# Install package in development mode
RUN pip install --user -e .

# Verify imports work correctly
RUN python -c "import iloveimg; print('✓ iloveimg import successful')"

# Default command: run all tests (JSON format for proper signal handling)
CMD ["sh", "-c", "pytest tests/unit && pytest tests/integration"]
