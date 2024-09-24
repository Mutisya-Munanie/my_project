# accounts/urls.py
# accounts/urls.py
from django.urls import path
from .views import custom_login  # Import your custom login view

urlpatterns = [
    path('login/', custom_login, name='custom_login'),  # Custom login URL
]





