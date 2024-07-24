from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Car

class CarAPITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.car1 = Car.objects.create(
            model='Corolla',
            brand='Toyota',
            price=20000.00,
            is_bought=False
        )
        cls.car2 = Car.objects.create(
            model='Civic',
            brand='Honda',
            price=22000.00,
            is_bought=True
        )

    def test_list_cars(self):
        url = reverse('car_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_car(self):
        url = reverse('car_list')
        data = {
            'model': 'Mustang',
            'brand': 'Ford',
            'price': 30000.00,
            'is_bought': False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Car.objects.count(), 3)

    def test_retrieve_car(self):
        url = reverse('car_detail', kwargs={'pk': self.car1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['model'], 'Corolla')

    def test_update_car(self):
        url = reverse('car_detail', kwargs={'pk': self.car1.pk})
        data = {
            'model': 'Corolla Updated',
            'brand': 'Toyota',
            'price': 21000.00,
            'is_bought': True
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.car1.refresh_from_db()
        self.assertEqual(self.car1.model, 'Corolla Updated')
        self.assertEqual(self.car1.price, 21000.00)
        self.assertTrue(self.car1.is_bought)

    def test_delete_car(self):
        url = reverse('car_detail', kwargs={'pk': self.car1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Car.objects.count(), 1)
