#from django.shortcuts import render

# Create your views here.



from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated  # Import IsAuthenticated permission
from .models import Order
from .serializers import OrderSerializer
from orders.sms_utils import send_sms_alert  # Ensure this import is correct
import logging

# Configure logging
logger = logging.getLogger(__name__)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Require authentication for this viewset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)

            # Send SMS alert after creating an order
            customer_phone_number = serializer.validated_data['customer'].phone_number
            item = serializer.validated_data['item']
            amount = serializer.validated_data['amount']

            # Ensure the phone number is valid before sending the SMS
            if customer_phone_number:
                try:
                    send_sms_alert(customer_phone_number, f"Order created: {item} - {amount:.2f}")
                except Exception as e:
                    logger.error(f"Failed to send SMS: {e}")
            else:
                logger.error("No phone number provided for the customer.")

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
