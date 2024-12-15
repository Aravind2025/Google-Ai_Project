# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the service account JSON file into the container for authentication
COPY service_account.json /app/service_account.json

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5001 for the Flask app
EXPOSE 5001

# Run the Flask app when the container starts
CMD ["python", "app.py"]

