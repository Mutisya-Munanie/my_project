#from django.db import models

# Create your models here.
# orders/models.py
# orders/models.py

from django.db import models
from customers.models import Customer
from .sms_utils import send_sms_alert_to_customer
from django.utils import timezone

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(null=True)  # Temporarily set to allow null values
    

    def save(self, *args, **kwargs):
        # Only initialize the API once for the entire process
        if not hasattr(Order, '_africastalking_initialized'):
            # This could call a method if needed; for now, the instance is already initialized in africas_talking.py
            Order._africastalking_initialized = True  # Set a flag to indicate initialization

        super().save(*args, **kwargs)  # Call the original save method

        # Send SMS after saving the order
        #send_sms_alert_to_customer(self.customer, self.item))


