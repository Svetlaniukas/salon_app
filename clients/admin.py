from django.contrib import admin
from .models import Client

# Admin interface for the Client model
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'avatar']  # Columns to display in the admin list view
    search_fields = ['user__username', 'phone']  # Fields to enable search functionality
