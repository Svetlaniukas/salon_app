from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')  # Establishes a one-to-one relationship with the User model
    name = models.CharField(max_length=100, default='Default Client Name')  # Default value for the name field
    email = models.EmailField(default='default@example.com')  # Default email value
    phone = models.CharField(max_length=15, blank=True, null=True)  # Makes the phone field optional
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # Optional avatar field with an upload path

    def __str__(self):
        return self.user.username  # Returns the username in the string representation
