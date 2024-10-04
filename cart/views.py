from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Cart
from cart_item.models import CartItem
from cart_item.serializers import CartItemSerializer
from .serializers import CartSerializer
from products.models import Products
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

# View to allow an authenticated user to add products to their cart
class AddToCart(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def post(self, request):
        user = request.user  # Get the authenticated user

        # Get or create a cart for the user
        cart, created = Cart.objects.get_or_create(user=user)
        product_id = request.data.get('product_id')  # Get product ID from the request data
        quantity = request.data.get('quantity')  # Get quantity from the request data

        # Validate that the product ID is provided
        if not product_id:
            return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the product or return a 404 if not found
        product = get_object_or_404(Products, id=product_id)

        with transaction.atomic():  # Ensure all database operations are atomic
            # Get or create a cart item for the specified product
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:  # If the item already exists in the cart, update the quantity
                cart_item.quantity += quantity  # Increment quantity
            else:
                cart_item.quantity = quantity  # Set quantity for new items

            # Update subtotal for the cart item
            cart_item.subtotal = cart_item.quantity * product.price
            cart_item.save()  # Save the cart item

            # Recalculate total price for the entire cart
            total_price = sum(item.subtotal for item in CartItem.objects.filter(cart=cart))
            cart.total_price = total_price  # Update the cart's total price
            cart.save()  # Save the cart

        return Response({"message": "Product added to cart", "total_price": cart.total_price}, status=status.HTTP_200_OK)

# View to retrieve all carts (primarily for admin or debugging purposes)
class GetAllCart(APIView):
    def get(self, request):
        # Fetch all cart records from the database
        cart = Cart.objects.all()
        
        # Serialize the cart data to a JSON-compatible format
        serializer = CartSerializer(cart, many=True)
        
        # Return the serialized data with a 200 OK response
        return Response(serializer.data, status=status.HTTP_200_OK)

# View to retrieve the cart for the currently authenticated user
class GetUserCart(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request):
        user = request.user  # Get the authenticated user
        try:
            # Retrieve the user's cart or raise a 404 if it doesn't exist
            cart = Cart.objects.get(user=user)
            cart_items = CartItem.objects.filter(cart=cart)  # Get items in the user's cart
            cart_serializer = CartSerializer(cart)  # Serialize cart data
            cart_items_serializer = CartItemSerializer(cart_items, many=True)  # Serialize cart items
            
            # Calculate total price on the fly
            total_price = sum(item.subtotal for item in cart_items)

            # Return the cart and items data along with total price
            return Response({
                "cart": cart_serializer.data,
                "cart_items": cart_items_serializer.data,
                "total_price": total_price  # Include total price in the response
            }, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            # Return an error message if the cart does not exist
            return Response({"message": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)

# View to clear all items from the user's cart
class ClearCart(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def delete(self, request):
        user = request.user  # Get the authenticated user
        # Get the user's cart or return a 404 if not found
        cart = get_object_or_404(Cart, user=user)  
        # Clear all items in the cart
        CartItem.objects.filter(cart=cart).delete()  

        return Response({"message": "Cart cleared successfully."}, status=status.HTTP_204_NO_CONTENT)

class UpdateCartItem(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        cart = get_object_or_404(Cart, user=user) # Get the user's cart
        product_id = request.data.get('product_id') # Get product ID from request data
        quantity = request.data.get('quantity') # Get the new quantity from request data

        if quantity is None:
            return Response({
                "error": 'Quantity is required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        product = get_object_or_404(Products, id=product_id) # Check if product exists
        cart_item = get_object_or_404(CartItem, cart=cart, product=product) # Get the cart item

        if quantity < 1: 
            cart_item.delete() # Remove the item from the cart if quantity less than 1
            return Response({"message": "Item removed from cart"}, status=status.HTTP_204_NO_CONTENT)
        
        else:
            # Update the quantity and subtotal
            cart_item.quantity = quantity
            cart_item.subtotal = cart_item.quantity * product.price # Recalculate the Subtotal
            cart_item.save()

            # Recalculate total price for the cart
            total_price = sum(item.subtotal for item in CartItem.objects.filter(cart=cart))
            cart.total_price = total_price
            cart.save()

            return Response({
                "message": "Cart item updated", "total_price": cart.total_price
            }, status=status.HTTP_200_OK)

class DeleteCartItem(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        cart = get_object_or_404(Cart, user=user)  # Get the user's cart
        product_id = request.data.get('product_id')  # Get product ID from request data

        product = get_object_or_404(Products, id=product_id)  # Check if product exists
        cart_item = get_object_or_404(CartItem, cart=cart, product=product)  # Get the cart item

        cart_item.delete()  # Remove item from cart

        # Recalculate total price for the cart
        total_price = sum(item.subtotal for item in CartItem.objects.filter(cart=cart))
        cart.total_price = total_price
        cart.save()

        return Response({"message": "Item deleted from cart", "total_price": cart.total_price}, status=status.HTTP_204_NO_CONTENT)