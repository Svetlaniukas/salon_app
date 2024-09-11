
# hairdressers/admin.py

from django.contrib import admin
from .models import Hairdresser

# Админка для модели парикмахера
@admin.register(Hairdresser)
class HairdresserAdmin(admin.ModelAdmin):
    list_display = ['user', 'specialization', 'experience']
    search_fields = ['user__username', 'specialization']
