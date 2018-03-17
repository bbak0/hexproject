from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

PREFERENCES = (('KD', 'Children'),
               ('EL', 'Elderly'),
               ('HO', 'Homeless'),
               ('TE', 'Tech'),
               ('MU', 'Music'),
               ('EV', 'Environmental'),
               ('ED', 'Educational'),
               )

class Volunteer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    bio = models.TextField(max_length = 500, blank = True)
	#phone_regex = RegexValidator(regex = r'^\+?1?\d{9,15}$', message = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #phone_number = models.CharField(validators = [phone_regex], max_length = 17, blank = True)
    location = models.CharField(max_length = 30, blank = True)
    birth_date = models.DateField(null = True, blank = True)
	#preferences = MultiSelectField(choices = PREFERENCES, max_choices = 7, max_length = 14)

class Benefactor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    bio = models.TextField(max_length = 500, blank = True)
    location = models.CharField(max_length = 30, blank = True)
	#phone_regex = RegexValidator(regex = r'^\+?1?\d{9,15}$', message = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #phone_number = models.CharField(validators = [phone_regex], max_length = 17, blank = True)

class Organizer(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	bio = models.TextField(max_length = 500, blank = True)
	location = models.CharField(max_length = 30, blank = True)
	verified = models.BooleanField(default = False)

class Events(models.Model):
	date = models.DateTimeField()
	title = models.CharField(max_length = 50)
	description = models.TextField()
	organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	'''objects = models.GeoManager()
    point = models.PointField(srid=4326)
    def latitude(self):
        return self.point.y
    def longitude(self):
        return self.point.x
'''
