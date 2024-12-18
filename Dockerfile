# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for Google Cloud Run
EXPOSE 8080

# Command to run the Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
