from django.contrib import admin
from .models import Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        "name",
        "description"
    )
    search_fields = ("name", "description")  # Optional: Add search functionality
    list_filter = ("name",)  # Optional: Add filters by category
