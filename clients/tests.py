from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserRegistrationTest(TestCase):
    def test_register_user(self):
        # Отправляем POST запрос на страницу регистрации клиента
        response = self.client.post(reverse('register_client'), {
            'username': 'testuser',
            'password1': 'ComplexPassword123!',
            'password2': 'ComplexPassword123!',
            'email': 'testuser@example.com'
        })

        # Проверяем, что пользователь был создан
        self.assertEqual(User.objects.count(), 1)
        
        # Проверяем редирект на панель управления клиента
        self.assertRedirects(response, reverse('client_dashboard'))
