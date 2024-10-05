from django.db import models
from django.contrib.auth.models import User

class Hairdresser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hairdresser_profile')
    name = models.CharField(max_length=100, default='Default Name')
    email = models.EmailField(default='default@example.com')
    phone = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    specialization = models.CharField(max_length=100, default='General Hairdresser')
    experience = models.PositiveIntegerField(default=0)
    availability = models.CharField(max_length=100, default='9 AM - 6 PM')

    # Method to calculate the average rating of the hairdresser
    def get_average_rating(self):
        reviews = self.reviews.all()  # Get all reviews for this hairdresser
        if reviews.exists():
            average = reviews.aggregate(models.Avg('rating'))['rating__avg']
            return round(average, 2)  # Round to two decimal places
        return 0  # If there are no reviews, return 0

    def __str__(self):
        return self.name  # String representation of the Hairdresser model
