from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)  # Retrieves the category name

    class Meta:
        model = Products
        fields = "__all__"

