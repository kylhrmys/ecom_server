from django.urls import path
from .views import GetAllCartItem

urlpatterns = [
    path('all/', GetAllCartItem.as_view(), name='get-all-cart-item')
]