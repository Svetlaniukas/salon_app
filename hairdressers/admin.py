from django.contrib import admin
from .models import Hairdresser

# Admin interface for the Hairdresser model
@admin.register(Hairdresser)
class HairdresserAdmin(admin.ModelAdmin):
    list_display = ['user', 'specialization', 'experience']  # Fields to display in the admin list view
    search_fields = ['user__username', 'specialization']  # Fields to enable search functionality
