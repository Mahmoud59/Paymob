from django.db import models


class Analysis(models.Model):
    key = models.CharField("Key", max_length=255)
    value = models.TextField("Value", null=True)
