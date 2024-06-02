# Use an appropriate base image for your application
FROM python:3.10.14

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

# Expose the port on which your FastAPI application will run (if applicable)
EXPOSE 3000

# Command to run your FastAPI application
CMD ["python", "app.py"]
