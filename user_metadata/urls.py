from django.urls import path
from .views import UserMetadataAddView, UserMetadataEditView, UserMetadataDeleteView

urlpatterns = [
    path("add/", UserMetadataAddView.as_view(), name="add-metadata"),
    path("edit/", UserMetadataEditView.as_view(), name="edit-metadata"),
     path("delete/", UserMetadataDeleteView.as_view(), name="delete-metadata"),
]
