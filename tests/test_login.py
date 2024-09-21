# tests/test_login.py
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTestCase(APITestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_success(self):
        url = reverse('account_login')  # Adjust this based on your URL pattern
        response = self.client.post(url, {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 200)  # or 302 if redirected
        self.assertIn('token', response.data)  # Example for token-based authentication

    def test_login_failure(self):
        url = reverse('account_login')  # Adjust this based on your URL pattern
        response = self.client.post(url, {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 400)  # or appropriate failure status

