from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User


class CredentialsAPIViewTestCase(APITestCase):

    def setUp(self):
        self.username = "admin2"
        self.password = "admin2"
        self.user = User.objects.create_user(self.username, self.password)
        self.token = self.user.auth_token
        self.api_authentication()
        self.credentials_data = dict(
            cea_login='login_cea',
            cima_login='login_cima',
        )

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_not_authenticated(self):
        response = APIClient().get('/codes/asfad/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



