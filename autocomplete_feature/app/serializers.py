from rest_framework import serializers
from .models import Credentials


class CredentialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credentials
        fields = ('cea_login', 'cima_login')

