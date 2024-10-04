from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Products


# View to handle the listing of all products
class ProductionListView(APIView):
    def get(self, request):
        # Retrieve all products from the database
        products = Products.objects.all()
        # Serialize the product data
        serializer = ProductSerializer(products, many=True)
        # Return the serialized data with a 200 OK status
        return Response(serializer.data, status=status.HTTP_200_OK)


# View to handle the addition of a new product
class ProductionAddView(APIView):
    def post(self, request):
        # Initialize the serializer with the request data
        serializer = ProductSerializer(data=request.data)
        # Validate the incoming data
        if serializer.is_valid():
            # Save the new product to the database
            serializer.save()
            # Return the serialized product data with a 201 Created status
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is invalid, return an error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View to retrieve a product by its ID
class ProductionGetProductById(APIView):
    def get(self, request, id):
        # Get the product or return a 404 error if it does not exist
        product = get_object_or_404(Products, pk=id)
        # Serialize the product data
        serializer = ProductSerializer(product)
        # Return the serialized product data
        return Response(serializer.data)


class ProductionEditProduct(APIView):
    def patch(self, request, id):
        # Get the product or return a 404 error if it does not exist
        product = get_object_or_404(Products, pk=id)

        # Create a serializer instance with the existing product instance and incoming request data
        # 'partial=True' allows updating only the fields that are present in the request
        serializer = ProductSerializer(product, data=request.data, partial=True)
        
        # Check if the serializer's data is valid (i.e., it passes the validation rules in the serializer)
        if serializer.is_valid():
            # If the data is valid, save the updated product
            serializer.save()
            
            # Return the updated product data in the response with HTTP 200 status
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # If the data is not valid, return the validation errors with HTTP 400 Bad Request status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to handle the deletion of a product
class ProductionDeleteProduct(APIView):
    def delete(self, request, id):
        # Attempt to find the product by ID
        product = Products.objects.filter(pk=id).first()
        if not product:
            # If the product does not exist, return an error response
            return Response({
                "error": f"Product with ID {id} does not exist"
            }, status=status.HTTP_400_BAD_REQUEST)
        # Delete the product
        product.delete()
        # Return a 204 No Content status to indicate successful deletion
        return Response(status=status.HTTP_204_NO_CONTENT)
