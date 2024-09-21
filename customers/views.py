#from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer # Ensure this import is correct

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=True, methods=['get'])
    def get_orders(self, request, pk=None):
        customer = self.get_object()
        orders = customer.order_set.all()  # Assuming related_name='order_set' in Order model
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

