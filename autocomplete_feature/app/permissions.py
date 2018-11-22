from django.conf import settings
from rest_framework import permissions


class IsValidToken(permissions.BasePermission):

    def has_permission(self, request, view):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token:
            return token.split()[1] == settings.TOKEN
        else:
            return False
