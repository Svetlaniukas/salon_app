# appointments/models.py

from django.db import models
from django.utils import timezone
from clients.models import Client  # Импортируем модель Client из приложения clients
from hairdressers.models import Hairdresser  # Импортируем модель Hairdresser из приложения hairdressers


class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='appointments')
    hairdresser = models.ForeignKey(Hairdresser, on_delete=models.CASCADE, related_name='appointments')
    service = models.CharField(max_length=100, choices=[
        ('haircut', 'Haircut'),
        ('coloring', 'Coloring'),
        ('manicure', 'Manicure'),
    ])

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Appointment for {self.client.user.username} with {self.hairdresser.user.username}"
