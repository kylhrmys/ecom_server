from rest_framework import serializers
from .models import UserMetadata

class UserMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMetadata
        exclude = ['user', 'id']