# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy only requirements.txt first (to leverage Docker cache)
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . /app/

# Ensure the database is ready before applying migrations and starting the server
CMD ["sh", "-c", "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 customers_orders_project.wsgi:application"]




