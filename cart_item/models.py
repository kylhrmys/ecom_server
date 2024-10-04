from django.db import models
from cart.models import Cart
from products.models import Products

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    subtotal = models.FloatField()

    def save(self, *args, **kwargs):
        # Automatically calculate subtotal based on product price and quantity
        self.subtotal = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Cart {self.cart.id} - Subtotal: ${self.subtotal:.2f}"
