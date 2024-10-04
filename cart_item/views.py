from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import CartItem
from .serializers import CartItemSerializer

# Create your views here.
class GetAllCartItem(APIView):
    def get(self, request):
        cart_item = CartItem.objects.all()
        serializer = CartItemSerializer(cart_item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        