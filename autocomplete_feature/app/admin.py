from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Credentials

admin.site.unregister(Group)


@admin.register(Credentials)
class CredentialsAdmin(admin.ModelAdmin):
    list_display = ('cea_login', 'cima_login')
    search_fields = ('cea_login', 'cima_login')



