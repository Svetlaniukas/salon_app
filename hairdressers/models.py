from django.db import models
from django.contrib.auth.models import User

class Hairdresser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hairdresser_profile')  # Добавьте related_name
    name = models.CharField(max_length=100, default='Default Name')  # Значение по умолчанию
    email = models.EmailField(default='default@example.com')  # Значение по умолчанию
    phone = models.CharField(max_length=15, blank=True, null=True)  # Делаем поле необязательным
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    # Добавляем недостающие поля
    specialization = models.CharField(max_length=100, default='General Hairdresser')  # Значение по умолчанию
    experience = models.PositiveIntegerField(default=0)  # Значение по умолчанию
    availability = models.CharField(max_length=100, default='9 AM - 6 PM')  # Значение по умолчанию

    def __str__(self):
        return self.name
