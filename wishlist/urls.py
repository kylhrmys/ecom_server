from django.urls import path
from .views import GetAllWishlist

urlpatterns = [
    path('all', GetAllWishlist.as_view(), name='get-all-wishlist')
]