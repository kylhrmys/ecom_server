from django.shortcuts import render
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Category
from django.shortcuts import get_object_or_404

# Create your views here.
class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serialzier = CategorySerializer(categories, many=True)
        return Response(serialzier.data, status=status.HTTP_200_OK)
    
class CategoryAddView(APIView):
    def post(self, request):
        # Initialize the serializer with the request data
        serializer = CategorySerializer(data=request.data)
        # Validate the incoming data
        if serializer.is_valid():
            # Save the new product to the database
            serializer.save()
            # Return the serialized product data with a 201 Created status
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is invalid, return an error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryEditView(APIView):
    # PATCH method is used for partial updates
    def patch(self, request, id):
        # Fetch the category object by its ID or return 404 if it doesn't exist
        category = get_object_or_404(Category, pk=id)
        
        # Create a serializer instance with the existing category instance and incoming request data
        # 'partial=True' allows updating only the fields that are present in the request
        serializer = CategorySerializer(category, data=request.data, partial=True)
        
        # Check if the serializer's data is valid (i.e., it passes the validation rules in the serializer)
        if serializer.is_valid():
            # If the data is valid, save the updated category
            serializer.save()
            
            # Return the updated category data in the response with HTTP 200 status
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # If the data is not valid, return the validation errors with HTTP 400 Bad Request status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryDeleteView(APIView):
    def delete(self, request, id):

        category = Category.objects.filter(pk=id).first()
        if not category:

            return Response({
                "error": f'Category with ID {id} does not exist'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        category.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)