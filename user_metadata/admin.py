from django.contrib import admin
from .models import UserMetadata

class UserMetadataAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'value', 'created_at', 'updated_at')  # Fields to display in the list view
    search_fields = ('user__username', 'key')  # Allow searching by username and key
    list_filter = ('user',)  # Filter by user in the admin interface
    ordering = ('created_at',)  # Order by created_at

# Register your models here
admin.site.register(UserMetadata, UserMetadataAdmin)
