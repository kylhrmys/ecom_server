from django.urls import path
from .views import GetAllOrderItem

urlpatterns = [
    path('all/', GetAllOrderItem.as_view(), name='get-all-order-item')
]