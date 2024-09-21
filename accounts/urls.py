# accounts/urls.py
from django.urls import path
from .views import profile  # Your profile view
from .auth import custom_login  # Your custom login view

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('login/', custom_login, name='custom_login'),  # Link to your custom login
]



