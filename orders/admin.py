from django.contrib import admin

# Register your models here.

from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'item', 'amount', )  # Adjust according to your fields
