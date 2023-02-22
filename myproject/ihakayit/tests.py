from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import IHA
from .serializers import IHASerializer

class IHAViewTests(APITestCase):
    def setUp(self):
        self.iha_data = {
            'brand': 'TestBrand',
            'model': 'TestModel',
            'weight': 1.5,
            'category': 'TestCategory'
        }
        self.iha = IHA.objects.create(**self.iha_data)
        self.url_list = reverse('iha-list')
        self.url_detail = reverse('iha-detail', kwargs={'pk': self.iha.pk})
        self.serializer_data = IHASerializer(self.iha).data
        self.valid_payload = {
            'brand': 'NewBrand',
            'model': 'NewModel',
            'weight': 2.0,
            'category': 'NewCategory'
        }

    def test_iha_list_view(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_iha_detail_view(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.serializer_data)

    def test_iha_create_view(self):
        response = self.client.post(self.url_list, data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(IHA.objects.count(), 2)
        self.assertEqual(IHA.objects.last().brand, self.valid_payload['brand'])

    def test_iha_update_view(self):
        response = self.client.put(self.url_detail, data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.iha.refresh_from_db()
        self.assertEqual(self.iha.brand, self.valid_payload['brand'])

    def test_iha_delete_view(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(IHA.objects.count(), 0)

    def test_iha_filter_view(self):
        response = self.client.get(self.url_list, {'brand': 'TestBrand'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
