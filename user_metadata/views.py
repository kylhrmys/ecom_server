from django.shortcuts import render
from .serializers import UserMetadataSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import UserMetadata
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserMetadataAddView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        key = request.data.get('key')
        value = request.data.get('value')

        # Validate input
        if not key or not value:
            return Response({
                "error": "Both key and value are requried"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if metadata with the same key already exists
        if UserMetadata.objects.filter(user=user, key=key).exists():
            return Response({
                "error": "Meta Data with this key already exists"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Create new metadata entry
        UserMetadata.objects.create(user=user, key=key, value=value)

        return Response({
            "message": "Metadata Added Successfully"
            }, status=status.HTTP_201_CREATED)
    
class UserMetadataEditView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        old_key = request.data.get('old_key')
        new_key = request.data.get('new_key')
        value = request.data.get('value')

        # Validate input
        if not old_key or not value:
            return Response({"error": "Old key and value are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve the existing metadata entry
            metadata = UserMetadata.objects.get(user=user, key=old_key)
            
            # Check if the new key already exists for this user
            if new_key and UserMetadata.objects.filter(user=user, key=new_key).exists():
                return Response({"error": "A metadata entry with the new key already exists."}, status=status.HTTP_400_BAD_REQUEST)

            # Update the key and value
            metadata.key = new_key if new_key else old_key  # Only change the key if new_key is provided
            metadata.value = value
            metadata.save()
            return Response({"message": "Metadata updated successfully"}, status=status.HTTP_200_OK)
        
        except UserMetadata.DoesNotExist:
            return Response({"error": "Metadata with the old key does not exist."}, status=status.HTTP_404_NOT_FOUND)

class UserMetadataDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        key = request.data.get('key')

        # Validate input
        if not key:
            return Response({"error": "Key is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve and delete the metadata entry
            metadata = UserMetadata.objects.get(user=user, key=key)
            metadata.delete()
            return Response({"message": "Metadata deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        
        except UserMetadata.DoesNotExist:
            return Response({"error": "Metadata with this key does not exist."}, status=status.HTTP_404_NOT_FOUND)
