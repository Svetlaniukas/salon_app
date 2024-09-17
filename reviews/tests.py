from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from clients.models import Client
from hairdressers.models import Hairdresser
from reviews.models import Review

class ReviewTest(TestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client_profile = Client.objects.create(user=self.user)
        self.hairdresser_user = User.objects.create_user(username='hairdresseruser', password='password123')
        self.hairdresser = Hairdresser.objects.create(user=self.hairdresser_user, specialization='Haircut')

        # URL для создания отзыва
        self.url = reverse('create_review', args=[self.hairdresser.id])

    def test_create_review(self):
        # Логиним пользователя
        self.client.login(username='testuser', password='password123')

        # Отправляем POST-запрос для создания отзыва
        response = self.client.post(self.url, {
            'rating': 5,
            'comment': 'Great service!',
        })

        # Проверяем статус ответа и количество созданных отзывов
        self.assertEqual(response.status_code, 302)  # Проверяем перенаправление
        self.assertEqual(Review.objects.count(), 1)
        review = Review.objects.first()
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, 'Great service!')
