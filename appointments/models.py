from django.db import models
from django.utils import timezone
from clients.models import Client  # Importing the Client model from the clients app
from hairdressers.models import Hairdresser  # Importing the Hairdresser model from the hairdressers app

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='appointments')  # Establishes a foreign key relationship with the Client model
    hairdresser = models.ForeignKey(Hairdresser, on_delete=models.CASCADE, related_name='appointments')  # Establishes a foreign key relationship with the Hairdresser model
    service = models.CharField(max_length=100, choices=[  # Defines the type of service for the appointment
        ('haircut', 'Haircut'),
        ('coloring', 'Coloring'),
        ('manicure', 'Manicure'),
    ])

    date = models.DateField()  # Appointment date
    start_time = models.TimeField()  # Appointment start time
    end_time = models.TimeField()  # Appointment end time

    def __str__(self):
        return f"Appointment for {self.client.user.username} with {self.hairdresser.user.username}"  # String representation of the appointment
