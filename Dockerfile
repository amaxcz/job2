# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory to /app
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y libpq-dev postgresql postgresql-contrib build-essential procps && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the initialization script to the container
COPY ./docker-entrypoint.sh /app/docker-entrypoint.sh

# Grant execute permissions to the script
RUN chmod +x /app/docker-entrypoint.sh

# Configure database URL
ENV DATABASE_URL='postgresql://demo1_user:demo1_pass@127.0.0.1:5432/demo1_db'

# Run the initialization script and start postgresql + uvicorn
CMD ["/app/docker-entrypoint.sh"]
