from django.urls import path
from .views import GetAllCart, AddToCart, GetUserCart, ClearCart, UpdateCartItem, DeleteCartItem

urlpatterns = [
    path('all/', GetAllCart.as_view(), name='get-all-cart'),
    path('my_cart/', GetUserCart.as_view(), name='get-user-cart'),
    path('add/', AddToCart.as_view(), name='add-to-cart' ),
    path('clear/', ClearCart.as_view(), name="clear-cart"),
    path('update_item/', UpdateCartItem.as_view(), name="update-item" ),
    path('delete-item/', DeleteCartItem.as_view(), name='delete-cart-item'),
]