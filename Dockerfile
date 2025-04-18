# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the Python script into the container
COPY server_get_post.py .

# Expose the port the app runs on
EXPOSE 8000

# Run the server
CMD ["python", "server_get_post.py"]
