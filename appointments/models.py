# appointments/models.py

from django.db import models
from django.utils import timezone
from clients.models import Client  # Импортируем модель Client из приложения clients
from hairdressers.models import Hairdresser  # Импортируем модель Hairdresser из приложения hairdressers

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='appointments')
    hairdresser = models.ForeignKey(Hairdresser, on_delete=models.CASCADE, related_name='appointments')
    service = models.CharField(max_length=100, choices=[
        ('стрижка', 'Стрижка'),
        ('покраска', 'Покраска'),
        ('маникюр', 'Маникюр'),
    ])
    date = models.DateField(default=timezone.now)
    start_time = models.TimeField(default='09:00:00')  # Добавили значение по умолчанию
    end_time = models.TimeField(default='12:00:00')  # Значение по умолчанию для поля end_time

    class Meta:
        unique_together = ('hairdresser', 'date', 'start_time')

    def __str__(self):
        return f"Appointment for {self.client.user.username} with {self.hairdresser.user.username} on {self.date} from {self.start_time} to {self.end_time}"
