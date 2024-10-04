from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import WishlistItem
from .serializers import WishlistItemSerializer

# Create your views here.
class GetAllWishlistItem(APIView):
    def get(self, request):
        wishlist_item = WishlistItem.objects.all()
        serializer = WishlistItemSerializer(wishlist_item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)