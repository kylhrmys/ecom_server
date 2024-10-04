from django.urls import path
from .views import (
    CategoryListView,
    CategoryAddView,
    CategoryEditView,
    CategoryDeleteView,
)

urlpatterns = [
    path('all/', CategoryListView.as_view(), name='get-all-category'),
    path('add/', CategoryAddView.as_view(), name='add-category'),
    path('edit/<int:id>/', CategoryEditView.as_view(), name='edit-category'),
    path('delete/<int:id>/', CategoryDeleteView.as_view(), name='delete-category'),
]