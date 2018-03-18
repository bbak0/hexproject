from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from multiselectfield import MultiSelectField

PREFERENCES = (('AE', 'Arts and Entertainment'),
               ('BZ','Business'),
               ('BP','Biological and Physical Sciences'),
               ('ED','Education'),
               ('EV','Environment'),
               ('GV','Government'),
               ('HM','Health &amp; Medicine'),
               ('IT','International'),
               ('LP','Law and Public Policy'),
               ('NP','Nonprofit'),
               ('SO','Society'),
               ('TC','Technology'))

class Volunteer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    bio = models.TextField(max_length = 500, blank = True)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length = 30, blank = True)
    birth_date = models.DateField(null = True, blank = True)
    preferences = MultiSelectField(choices = PREFERENCES, max_choices = 12, max_length = 24, default = None)

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
