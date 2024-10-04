from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Wishlist
from .serializers import WishlistSerializer

# Create your views here.
class GetAllWishlist(APIView):
    def get(self, request):
        wishlist = Wishlist.objects.all()
        serializer = WishlistSerializer(wishlist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)