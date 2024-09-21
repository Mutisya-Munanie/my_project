# Makefile for managing environment variables and common tasks

# Load environment variables
export $(shell cat .env | xargs)

# Command to run Django development server
run:
    python manage.py runserver

# Command to run tests
test:
    python manage.py test

# Command to apply migrations
migrate:
    python manage.py migrate

# Command to create a superuser
createsuperuser:
    python manage.py createsuperuser
