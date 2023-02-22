from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class UserRegistrationViewTestCase(APITestCase):

    def test_user_registration(self):
        url = reverse('user-registration')
        data = {
            'email': 'test@test.com',
            'password': 'test123',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='test@test.com',
            password='test123'
        )

    def test_user_login(self):
        url = reverse('login')
        data = {
            'email': 'test@test.com',
            'password': 'test123',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_login_invalid_credentials(self):
        url = reverse('login')
        data = {
            'email': 'test@test.com',
            'password': 'wrongpassword',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LogoutViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='test@test.com',
            password='test123'
        )
        self.client.login(email='test@test.com', password='test123')

    def test_user_logout(self):
        url = reverse('logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
