# common_utils.py
from .africas_talking import africa_talking_instance

def send_sms_alert(phone_number, message):
    """
    Sends an SMS alert to the specified phone number.
    """
    africa_talking_instance.send_sms(phone_number, message)

def initialize_africastalking():
    """
    Initialize Africa's Talking instance if necessary.
    """
    # Since africa_talking_instance is already initialized in africas_talking.py,
    # you can leave this function empty or remove it if not needed.
    pass
