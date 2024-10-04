from django.db import models
from order.models import Order
from products.models import Products

# Create your models here.
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_at_purchase = models.FloatField() #Price of the product at the time of purchase

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Order {self.order.id}"
