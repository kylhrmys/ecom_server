from django.urls import path
from .views import (
    ProductionListView,
    ProductionAddView,
    ProductionGetProductById,
    ProductionEditProduct,
    ProductionDeleteProduct,
)

urlpatterns = [
    path('all/', ProductionListView.as_view(), name="product-list"),
    path('add/', ProductionAddView.as_view(), name="product-add"),
    path('edit/<int:id>/', ProductionEditProduct.as_view(), name="product-edit"),
    path('<int:id>/', ProductionGetProductById.as_view(), name="product-by-id"),
    path('delete/<int:id>/', ProductionDeleteProduct.as_view(), name="product-delete"),
]