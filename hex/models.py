from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from multiselectfield import MultiSelectField

PREFERENCES = {'1' : 'Arts and Entertainment',
               '2' : 'Business',
               '3' : 'Biological and Physical Sciences',
               '4' : 'Education',
               '5' : 'Environment',
               '6' : 'Government',
               '7' : 'Health &amp; Medicine',
               '8' : 'International',
               '9' : 'Law and Public Policy',
               '10' : 'Nonprofit',
               '11' : 'Society',
               '12' : 'Technology'}

class Volunteer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    bio = models.TextField(max_length = 500, blank = True)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length = 30, blank = True)
    birth_date = models.DateField(null = True, blank = True)
    preferences = models.CharField(max_length = 40, blank = True)

class Benefactor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    bio = models.TextField(max_length = 500, blank = True)
    location = models.CharField(max_length = 30, blank = True)
    phone_number = models.CharField(max_length=15)

class Organizer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    bio = models.TextField(max_length = 500, blank = True)
    location = models.CharField(max_length = 30, blank = True)
    verified = models.BooleanField(default = False)
    phone_number = models.CharField(max_length = 15)

class Events(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length = 50)
    description = models.TextField()
    city = models.TextField()
    adress = models.TextField()
    duration = models.TextField()
    type = models.CharField(max_length=2)
    #Picture
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

class EventRegistration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    event = models.ForeignKey(Events, on_delete = models.CASCADE)
