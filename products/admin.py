from django.contrib import admin
from .models import Products


# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "quantity",
        "category",
        "sku",
        "created_at",
        "updated_at",
    )
    search_fields = ("name", "category", "sku")  # Optional: Add search functionality
    list_filter = ("category",)  # Optional: Add filters by category
