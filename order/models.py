from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_price = models.FloatField()
    payment_status = models.CharField(max_length=200)  # e.g., "Paid", "Pending", etc.
    delivery_method = models.CharField(max_length=200)  # e.g., "Delivery", "Pickup"
    order_status = models.CharField(max_length=200)  # e.g., "Processing", "Shipped", "Completed"
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set when updated

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

