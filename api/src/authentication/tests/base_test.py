import json

from rest_framework.test import APIClient
from django.test import TestCase
from api.src.authentication.models import User


class BaseTest(TestCase):

    def setUp(self):

        self.LOGIN_URL = '/api/v1/auth/login/'
        self.REGISTER_URL = '/api/v1/auth/register/'
        self.COCKTAIL_LIST_URL='/api/v1/cocktail/list/'
        self.COCKTAIL_RETRIEVE_URL='/api/v1/cocktail/retrieve/'
        self.COCKTAIL_CREATE_URL='/api/v1/cocktail/create/'



        self.register_data = {
                "username": "mathias",
                "email": "mathias@gmail.com",
                "password": "mathias2"
            }


        self.new_user1 = User(
            username='james',
            email='james@yahoo.com',
            password=1234
        )

        self.test_user1 = {
            'username':'test',
            'email':'test@test.com',
            'password':'test12'
        }


        self.client = APIClient()

        ress=self.client.post(self.REGISTER_URL, self.test_user1, format="json")
        res = self.client.post(self.LOGIN_URL, self.test_user1, format="json")
        self.access_token = "Bearer " + eval(res.data['tokens'])['access']
        self.user_id = str(ress.data['id'])
    