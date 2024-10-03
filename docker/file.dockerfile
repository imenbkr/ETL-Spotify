# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies (optional)
RUN apt-get update && apt-get install -y cron

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the required port (if using Redash or other web tools)
EXPOSE 5000

# Set environment variables from the .env file (if needed)
COPY .env /app/.env

# Set up cron job (optional)
COPY cron_schedule.sh /etc/cron.d/spotify-etl-cron
RUN chmod 0644 /etc/cron.d/spotify-etl-cron
RUN crontab /etc/cron.d/spotify-etl-cron

# Define the default command to run when the container starts
CMD ["python", "etl_pipeline.py"]
