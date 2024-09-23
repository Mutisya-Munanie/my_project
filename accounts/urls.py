# accounts/urls.py
from django.urls import path
from .views import ProfileView, profile_update  # Your profile view
from .auth import custom_login  # Your custom login view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login view
    path('login/', custom_login, name='custom_login'),  # Link to your custom login
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', profile_update, name='profile_update'),  # Add this line
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),  # Logout view
]




