# tests/test_sms.py

#Unit Tests for Africa’s Talking SMS (Mocking the API)

from django.test import TestCase
from unittest.mock import patch
from orders.sms_utils import send_sms_alert_to_customer  # Import the actual function you want to test
from customers.models import Customer
from orders.models import Order

class SMSTestCase(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe", phone_number="+254797192576", code="CUST001")

    @patch('orders.sms_utils.send_sms_alert')
    def test_sms_sent_on_order(self, mock_send_sms_alert):
        # Create an order
        order = Order.objects.create(customer=self.customer, item="Test Item", amount=100.0)

        # Act: Call the function that sends the SMS alert
        send_sms_alert_to_customer(self.customer, order.item)

        # Assert that the SMS function was called
        mock_send_sms_alert.assert_called_once_with(self.customer.phone_number, "Dear John Doe, your order for Test Item has been received.")

if __name__ == '__main__':
    unittest.main()

