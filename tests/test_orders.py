#from django.test import TestCase

# Create your tests here.

# Unit Tests for Models (Orders)
from django.test import TestCase
from orders.models import Order
from customers.models import Customer
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APITestCase
from datetime import datetime
from django.contrib.auth import get_user_model
from unittest.mock import patch  # Import for mocking

# Unit test for the Order Model
class OrderModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(name="Jade Kay", code="CUST001", phone_number="+254797192576")
        print(self.customer.phone_number)

    def test_order_creation(self):
        order = Order.objects.create(
            customer=self.customer,
            item="Test Item",
            amount=1000.0,
            time=timezone.now()  
        )
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.item, "Test Item")
        self.assertEqual(order.amount, 1000.0)
        self.assertTrue(order.time)  # Ensure the order has a timestamp


# Unit Tests for REST API Views (Orders)
class OrderAPITest(APITestCase):

    def setUp(self):
        self.customer = Customer.objects.create(name="Jade Kay", code="CUST001", phone_number="+254797192576")
        # Create a user for authentication
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')  # Log in the user

    @patch('orders.africas_talking.africa_talking_instance.send_sms')  # Mock Africa's Talking SMS
    def test_create_order(self, mock_send_sms):  # Add mock_send_sms as a parameter
        mock_send_sms.return_value = {'status': 'success'}  # Mock the SMS sending response
        url = reverse('order-list')  # Adjust to your API view name
        data = {
            "customer": self.customer.id,
            "item": "Test Item",
            "amount": 1000.0,
            "time": timezone.now().isoformat()  # Ensure correct timezone handling
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().item, 'Test Item')

    def test_list_orders(self):
        Order.objects.create(customer=self.customer, item="Test Item", amount=1000.0, time=timezone.now())
        url = reverse('order-list')  
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


