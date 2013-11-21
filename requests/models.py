from django.db import models


class Request(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=100)
    method = models.CharField(max_length=8)
