from django.test import TestCase

# Create your tests here.

# from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status

class AccountsTest(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user('testboi', 'testboi@example.com', 'passboi')
        self.create_url = reverse('account-create')

    def test_create_user(self):
        data = {
            'username': 'rikki lake',
            'password': 'floydboi'
        }

        response = self.client.post(self.create_url , data, format='json')

        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertFalse('password' in response.data)
