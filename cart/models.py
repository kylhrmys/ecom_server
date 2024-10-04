from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.FloatField(default=0.0)  # Add this field

    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"
