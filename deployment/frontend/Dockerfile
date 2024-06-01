# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Install any dependencies required for your application
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the source code and any other necessary files into the container
COPY src/ .

# Define environment variable
ENV NAME DashApp

# Run app.py when the container launches
CMD ["python", "app.py"]
