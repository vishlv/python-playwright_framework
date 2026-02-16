# Use the official Playwright Python image
FROM mcr.microsoft.com/playwright/python:v1.50.0-noble

# Set environment variables to prevent Python from writing .pyc files and buffering output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first (for better Docker caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project code
COPY . .

# Run your tests using pytest
CMD ["pytest"]