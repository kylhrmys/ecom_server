from django.urls import path
from .views import GetAllWishlistItem

urlpatterns = [
    path('all', GetAllWishlistItem.as_view(), name='get-all-wishlist-item')
]