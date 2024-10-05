from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserRegistrationTest(TestCase):
    def test_register_user(self):
        # Send a POST request to the client registration page
        response = self.client.post(reverse('register_client'), {
            'username': 'testuser',
            'password1': 'ComplexPassword123!',
            'password2': 'ComplexPassword123!',
            'email': 'testuser@example.com'
        })

        # Check if the user was created
        self.assertEqual(User.objects.count(), 1)
        
        # Check if the user is redirected to the client dashboard
        self.assertRedirects(response, reverse('client_dashboard'))
