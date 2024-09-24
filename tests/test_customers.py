#from django.test import TestCase

# Create your tests here.

#Unit Tests for Models (Customers)
from django.test import TestCase
from customers.models import Customer

class CustomerModelTest(TestCase):

    def test_customer_creation(self):
        customer = Customer.objects.create(name="Jade Kay", code="CUST001")
        self.assertEqual(customer.name, "Jade Kay")
        self.assertEqual(customer.code, "CUST001")
        self.assertTrue(customer.id)  


#Unit Tests for REST API Views (Customers)
from django.urls import reverse
from rest_framework.test import APITestCase
from customers.models import Customer

class CustomerAPITest(APITestCase):

    def test_create_customer(self):
        url = reverse('customer-list')  # Adjusted according to my API view name
        data = {"name": "Sally Kay", "code": "CUST002"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, 'Sally Kay')

    def test_list_customers(self):
        Customer.objects.create(name="Jade Kay", code="CUST001")
        url = reverse('customer-list')  
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
