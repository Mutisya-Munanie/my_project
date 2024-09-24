
  # tests/test_auth.py
# tests/test_auth.py
import json
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class AuthTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        
        # Ensure the URL for custom login is correct
        self.url = reverse('custom_login')  # Ensure this matches the name in your urls.py

    def test_login_success(self):
        # Prepare the data for login
        data = {'username': self.username, 'password': self.password}
        
        # Perform the login request
        response = self.client.post(self.url, data, format='json')
        
        # Check for a successful login response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'Login successful')

    def test_login_invalid_credentials(self):
        # Prepare the data with invalid credentials
        data = {'username': 'wronguser', 'password': 'wrongpassword'}
        
        # Perform the login request
        response = self.client.post(self.url, data, format='json')
        
        # Check for an error response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'Invalid credentials')

# Add more tests for other functionalities if needed
