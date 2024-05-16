from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.test import APIClient

from .models import Play, TheatreHall, Performance, Ticket, Reservation

class ModelTests(TestCase):

    def test_play_string_representation(self):
        play = Play.objects.create(title="Hamlet", description="A Shakespeare play")
        self.assertEqual(str(play), "Hamlet")

    def test_theatre_hall_capacity(self):
        hall = TheatreHall.objects.create(name="Main", rows=10, seats_in_row=10)
        self.assertEqual(hall.capacity, 100)


class ViewSetTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="user@email.com", password="testpass"
        )
        self.client.force_authenticate(user=self.user)

    def test_retrieve_play_list_unauthenticated(self):
        self.client.logout()
        url = reverse("theater:play-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_play_list_authenticated(self):
        url = reverse("theater:play-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_performance_as_admin(self):
        admin = get_user_model().objects.create_superuser(
            email="admin@example.com", password="adminpass"
        )
        self.client.force_authenticate(user=admin)
        play = Play.objects.create(title="Hamlet", description="A Shakespeare play")
        hall = TheatreHall.objects.create(name="Main", rows=10, seats_in_row=20)
        url = reverse("theater:performance-list")
        data = {
            "play": play.id,
            "theatre_hall": hall.id,
            "show_time": "2023-01-01T10:00:00Z",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
