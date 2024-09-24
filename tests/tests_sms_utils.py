
 # tests/test_sms_utils.py


# test_sms_utils.py
import unittest
from unittest.mock import patch
from collections import namedtuple
from orders.sms_utils import send_sms_alert_to_customer  # Adjust the import based on your project structure

# Create a simple Customer class for testing
Customer = namedtuple('Customer', ['name', 'phone_number'])

class TestSmsUtils(unittest.TestCase):

    @patch('orders.sms_utils.send_sms_alert')
    def test_send_sms_alert_to_customer(self, mock_send_sms_alert):
        # Arrange
        customer = Customer(name='John Doe', phone_number='+254797192576')
        item = 'Laptop'

        # Act
        send_sms_alert_to_customer(customer, item)

        # Assert
        expected_message = f"Dear {customer.name}, your order for {item} has been received."
        mock_send_sms_alert.assert_called_once_with(customer.phone_number, expected_message)

if __name__ == '__main__':
    unittest.main()
