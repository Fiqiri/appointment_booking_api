from django.test import TestCase
from rest_framework.test import APIClient
from .models import Doctor


class DoctorTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.doctor = Doctor.objects.create(name="Dr. John", start_time="09:00", end_time="17:00")

    def test_list_doctors(self):
        response = self.client.get('/doctors/')
        self.assertEqual(response.status_code, 200)

    def test_create_doctor(self):
        data = {"name": "Dr. Jane", "start_time": "10:00", "end_time": "18:00"}
        response = self.client.post('/doctors/create/', data)
        self.assertEqual(response.status_code, 201)
