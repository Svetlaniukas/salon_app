from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Hairdresser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    experience_years = models.IntegerField()

    def __str__(self):
        return self.user.username
