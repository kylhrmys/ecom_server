from django.urls import path
from .views import GetAllOrder

urlpatterns = [
    path('all/', GetAllOrder.as_view(), name='get-all-order')
]