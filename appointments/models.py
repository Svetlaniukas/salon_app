from django.db import models

# Create your models here.
from django.db import models
from clients.models import Client
from hairdressers.models import Hairdresser

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    hairdresser = models.ForeignKey(Hairdresser, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.client.user.username} - {self.service} - {self.date_time}"
