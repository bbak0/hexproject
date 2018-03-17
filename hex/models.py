from django.db import models

class events(models.Model):
	date = models.DateField()
	x_coordinate = models.DoubleField(null=True)
	y_coordinate = models.DoubleField(null=True)
	title = models.CharField(max_length = 50)
	description = models.TextField()
	organizer = models.ForeignKey()
