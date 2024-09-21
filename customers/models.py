#from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)  # Add this field

    def __str__(self):
        return self.name


