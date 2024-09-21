import pytest
from django.urls import reverse
from customers.models import Customer
from orders.models import Order

@pytest.mark.django_db
def test_add_customer(client):
    response = client.post(reverse('customer-list'), data={'name': 'John Doe', 'code': 'CUST001'})
    assert response.status_code == 201

@pytest.mark.django_db
def test_add_order(client):
    customer = Customer.objects.create(name='John Doe', code='CUST001')
    response = client.post(reverse('order-list'), data={'item': 'Laptop', 'amount': 1000.0, 'customer': customer.id})
    assert response.status_code == 201
