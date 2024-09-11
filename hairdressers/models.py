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

    # Метод для вычисления среднего рейтинга парикмахера
    def get_average_rating(self):
        reviews = self.reviews.all()  # Получаем все отзывы для этого парикмахера
        if reviews.exists():
            average = reviews.aggregate(models.Avg('rating'))['rating__avg']
            return round(average, 2)  # Округляем до двух знаков
        return 0  # Если отзывов нет, возвращаем 0

    def __str__(self):
        return self.name
