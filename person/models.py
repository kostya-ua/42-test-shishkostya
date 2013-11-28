from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20, blank=True)
    bithdate = models.DateField()
    bio = models.TextField(blank=True)
    email = models.EmailField()
    skype = models.CharField(max_length=20, blank=True)
    jabber = models.CharField(max_length=40, blank=True)
    other_contacts = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True)