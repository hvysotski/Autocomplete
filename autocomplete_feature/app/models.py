from django.db import models


class Credentials(models.Model):

    class Meta:
        verbose_name_plural = 'Credentials'

    cea_login = models.CharField(max_length=30)
    cima_login = models.CharField(max_length=30)
