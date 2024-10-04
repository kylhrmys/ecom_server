from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Order
from .serializers import OrderSerializer

# Create your views here.
class GetAllOrder(APIView):
    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)