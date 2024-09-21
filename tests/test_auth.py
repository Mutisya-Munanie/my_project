
  # tests/test_auth.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class AuthTestCase(APITestCase):
    
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_success(self):
        url = reverse('account_login')  # Make sure this matches your allauth URL
        response = self.client.post(url, {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # or 302 if it redirects
        self.assertContains(response, 'Login successful')  # Adjust this based on your actual response

    def test_login_failure(self):
        url = reverse('account_login')  # Ensure this matches your allauth URL
        response = self.client.post(url, {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Adjust if necessary
        self.assertContains(response, 'Invalid credentials')  # Adjust based on actual response

