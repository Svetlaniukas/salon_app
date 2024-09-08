from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    name = models.CharField(max_length=100, default='Default Client Name')  # Значение по умолчанию
    email = models.EmailField(default='default@example.com')  # Значение по умолчанию
    phone = models.CharField(max_length=15, blank=True, null=True)  # Делаем поле необязательным
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username  # Отображаем имя пользователя в __str__
