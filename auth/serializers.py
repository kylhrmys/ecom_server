from rest_framework import serializers
from django.contrib.auth.models import User
from user_metadata.models import UserMetadata
from user_metadata.serializers import UserMetadataSerializer

class UserSerializer(serializers.ModelSerializer):
    metadata = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ['password']  # Only use exclude or fields, not both

    # merge from user_metadata module
    def get_metadata(self, obj):
        metadata_qs = UserMetadata.objects.filter(user=obj)
        serializer = UserMetadataSerializer(metadata_qs, many=True)
        return serializer.data
