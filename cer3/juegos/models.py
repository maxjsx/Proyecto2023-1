from django.db import models


class Games(models.Model):
    name = models.CharField(max_length=200)
    loaned = models.BooleanField()

