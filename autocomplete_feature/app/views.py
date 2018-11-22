from rest_framework import viewsets, mixins
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .serializers import CredentialsSerializer
from .permissions import IsValidToken
from .models import Credentials


class CredentialsViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for viewing and editing credentials.
    """
    serializer_class = CredentialsSerializer
    permission_classes = (IsValidToken, )

    def get_object(self):
        login = self.kwargs.get('login')
        return get_object_or_404(Credentials.objects.filter(Q(cea_login=login) | Q(cima_login=login)))

