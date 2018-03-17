from django.db import models

class Events(models.Model):
	date = models.DateTimeField()
	x_coordinate = models.DoubleField(null=True)
	y_coordinate = models.DoubleField(null=True)
	title = models.CharField(max_length = 50)
	description = models.TextField()
	organizer = models.ForeignKey(settings.AUTH_USER_MODEL)
