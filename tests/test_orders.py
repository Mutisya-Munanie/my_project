#from django.test import TestCase

# Create your tests here.

# Unit Tests for Models (Orders)
from django.test import TestCase
from orders.models import Order
from customers.models import Customer
from django.utils import timezone

class OrderModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe", code="CUST001", phone_number="+254797192576")

    def test_order_creation(self):
        order = Order.objects.create(
            customer=self.customer,
            item="Test Item",
            amount=100.0,
            time=timezone.now()  
        )
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.item, "Test Item")
        self.assertEqual(order.amount, 100.0)
        self.assertTrue(order.time)  # Ensure the order has a timestamp


# Unit Tests for REST API Views (Orders)
from django.urls import reverse
from rest_framework.test import APITestCase
from customers.models import Customer
from orders.models import Order
from datetime import datetime
from django.utils import timezone  # Import timezone for consistency
from django.contrib.auth import get_user_model

class OrderAPITest(APITestCase):

    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe", code="CUST001")
        # Create a user for authentication
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')  # Log in the user

    def test_create_order(self):
        url = reverse('order-list')  # Adjust to your API view name
        data = {
            "customer": self.customer.id,
            "item": "Test Item",
            "amount": 100.0,
            "time": timezone.now().isoformat()  # Ensure correct timezone handling
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().item, 'Test Item')

    def test_list_orders(self):
        Order.objects.create(customer=self.customer, item="Test Item", amount=100.0, time=timezone.now())
        url = reverse('order-list')  # Adjust to your API view name
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)



