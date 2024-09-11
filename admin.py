# hairdresser_project/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from clients.models import Client
from hairdressers.models import Hairdresser

# Создаем инлайн для отображения профиля клиента
class ClientInline(admin.StackedInline):
    model = Client
    can_delete = False
    verbose_name_plural = 'Clients'

# Создаем инлайн для отображения профиля парикмахера
class HairdresserInline(admin.StackedInline):
    model = Hairdresser
    can_delete = False
    verbose_name_plural = 'Hairdressers'

# Переопределяем админку для User, добавляем инлайн профили клиента и парикмахера
# hairdresser_project/admin.py

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_client', 'is_hairdresser')

    def is_client(self, obj):
        return hasattr(obj, 'client_profile')
    is_client.short_description = 'Is Client'
    is_client.boolean = True

    def is_hairdresser(self, obj):
        return hasattr(obj, 'hairdresser_profile')
    is_hairdresser.short_description = 'Is Hairdresser'
    is_hairdresser.boolean = True

# Снова перерегистрируем UserAdmin с новыми полями
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
