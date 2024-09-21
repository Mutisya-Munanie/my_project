# sms_utils.py
from .common_utils import send_sms_alert

def send_sms_alert_to_customer(customer, item):
    """
    Sends an SMS alert to the customer's phone number.
    """
    message = f"Dear {customer.name}, your order for {item} has been received."
    send_sms_alert(customer.phone_number, message)



