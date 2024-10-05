from django.db import models
from clients.models import Client  # Importing the Client model from the clients app
from hairdressers.models import Hairdresser  # Importing the Hairdresser model from the hairdressers app

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)  
    hairdresser = models.ForeignKey(Hairdresser, on_delete=models.CASCADE, related_name='appointments')  
    service = models.CharField(max_length=100, choices=[
        ('haircut', 'Haircut'),
        ('coloring', 'Coloring'),
        ('manicure', 'Manicure'),
    ])

    date = models.DateField()  # Appointment date
    start_time = models.TimeField()  # Appointment start time
    end_time = models.TimeField()  # Appointment end time

    def __str__(self):
        if self.client:
            return f"Appointment for {self.client.user.username} with {self.hairdresser.user.username}"
        else:
            return f"Appointment with {self.hairdresser.user.username} (no client)"  
