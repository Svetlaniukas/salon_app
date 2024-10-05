from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from clients.models import Client
from hairdressers.models import Hairdresser

# Create an inline to display the client profile
class ClientInline(admin.StackedInline):
    model = Client
    can_delete = False
    verbose_name_plural = 'Clients'

# Create an inline to display the hairdresser profile
class HairdresserInline(admin.StackedInline):
    model = Hairdresser
    can_delete = False
    verbose_name_plural = 'Hairdressers'

# Override the admin for User, adding inline profiles for client and hairdresser
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

# Re-register the UserAdmin with the new fields
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
