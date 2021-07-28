from rest_framework import status
from api.src.authentication.tests.base_test import BaseTest

class CocktailTests(BaseTest):
    def test_can_get_all_cocktails(self):
        res= self.client.get(self.COCKTAIL_LIST_URL,format="json")
        self.assertEqual(res.status_code,status.HTTP_200_OK)

    def test_can_get_user_cocktails(self):
        res= self.client.get(self.COCKTAIL_RETRIEVE_URL,
        HTTP_AUTHORIZATION=self.access_token,format="json")
        self.assertEqual(res.status_code,status.HTTP_200_OK)

    def test_can_creat_cocktail(self):
        data = {
            "name": "Delmonte",
            "price": 205.00
        }
        res= self.client.post(self.COCKTAIL_CREATE_URL,
        data,HTTP_AUTHORIZATION=self.access_token,format="json")
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
