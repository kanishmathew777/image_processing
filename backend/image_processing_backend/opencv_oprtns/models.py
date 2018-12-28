from django.db import models


class Filesave(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(null=False, blank=False, max_length=200,)
