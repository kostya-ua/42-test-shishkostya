from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    bithdate = models.DateField()
    bio = models.TextField()
    email = models.CharField(max_length=20)
    skype = models.CharField(max_length=20)
    jabber = models.CharField(max_length=20)
    other_contacts = models.TextField()
