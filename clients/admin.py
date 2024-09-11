
# clients/admin.py

from django.contrib import admin
from .models import Client

# Админка для модели клиента
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'avatar']
    search_fields = ['user__username', 'phone']

