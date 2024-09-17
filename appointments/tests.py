from django.test import TestCase
from django.urls import reverse
from clients.models import Client
from hairdressers.models import Hairdresser
from appointments.models import Appointment
from django.contrib.auth.models import User

class AppointmentTest(TestCase):
    def setUp(self):
        self.client_user = Client.objects.create(user=self.create_user('client_user'))
        self.hairdresser_user = Hairdresser.objects.create(user=self.create_user('hairdresser_user'))
        self.url = reverse('create_appointment')

    def create_user(self, username):
        return User.objects.create_user(username=username, password='password123', email=f'{username}@test.com')

    def test_create_appointment(self):
        self.client.login(username='client_user', password='password123')
        response = self.client.post(self.url, {
            'service': 'haircut',
            'start': '2024-09-20T10:00',
            'end': '2024-09-20T11:00',
            'hairdresser': self.hairdresser_user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Appointment.objects.count(), 1)
