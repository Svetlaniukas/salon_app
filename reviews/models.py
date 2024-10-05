from django.db import models
from django.contrib.auth.models import User  # Using the User model
from hairdressers.models import Hairdresser  # Importing the Hairdresser model

class Review(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)  # The client who leaves the review
    hairdresser = models.ForeignKey(Hairdresser, on_delete=models.CASCADE, related_name='reviews')  # The hairdresser receiving the review
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating from 1 to 5
    comment = models.TextField()  # Field for the review comment
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically adds the creation date and time

    def __str__(self):
        return f"Review by {self.client.username} for {self.hairdresser.user.username}"
