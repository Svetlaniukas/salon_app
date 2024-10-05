from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from clients.models import Client
from hairdressers.models import Hairdresser
from reviews.models import Review

class ReviewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client_profile = Client.objects.create(user=self.user)
        self.hairdresser_user = User.objects.create_user(username='hairdresseruser', password='password123')
        self.hairdresser = Hairdresser.objects.create(user=self.hairdresser_user, specialization='Haircut')

        # URL for creating a review
        self.url = reverse('create_review', args=[self.hairdresser.id])

    def test_create_review(self):
        # Log in the user
        self.client.login(username='testuser', password='password123')

        # Send a POST request to create a review
        response = self.client.post(self.url, {
            'rating': 5,
            'comment': 'Great service!',
        })

        # Check the response status and the number of created reviews
        self.assertEqual(response.status_code, 302)  # Check the redirect
        self.assertEqual(Review.objects.count(), 1)
        review = Review.objects.first()
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, 'Great service!')
