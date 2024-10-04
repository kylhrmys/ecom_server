from django.db import models
from wishlist.models import Wishlist
from products.models import Products

# Create your models here.
class WishlistItem(models.Model):
    Wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} in {self.wishlist.user.username}\'s wishlist'
