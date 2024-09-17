from django.db import models
from django.contrib.auth.models import User  # Используем модель пользователя
from hairdressers.models import Hairdresser  # Импортируем модель парикмахера

class Review(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)  # Клиент, который оставляет отзыв
    hairdresser = models.ForeignKey(Hairdresser, on_delete=models.CASCADE, related_name='reviews')  # Парикмахер, который получает отзыв
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])  # Рейтинг от 1 до 5
    comment = models.TextField()  # Поле для текста отзыва
    created_at = models.DateTimeField(auto_now_add=True)  # Автоматически добавляет дату и время создания отзыва

    def __str__(self):
        return f"Review by {self.client.username} for {self.hairdresser.user.username}"
