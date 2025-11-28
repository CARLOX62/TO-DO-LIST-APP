# Base Python Image
FROM python:3.10-slim

# Disable .pyc files and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Install OS dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Copy requirements first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose port Flask/Gunicorn will use
EXPOSE 5000

# Start Gunicorn server (Main entry is run.py with app object inside create_app)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
