from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import OrderItem
from .serializers import OrderItemSerializer

# Create your views here.
class GetAllOrderItem(APIView):
    def get(self, request):
        order_item = OrderItem.objects.all()
        serializer = OrderItemSerializer(order_item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)