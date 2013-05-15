from django.db import models

class Place(models.Model):
	name = models.CharField(max_length = 50)
	address = models.CharField(max_length = 100)
	
	def __unicode__(self):
		return u"%s the place" % self.name


class Restaurant(models.Model):
	place = models.OneToOneField(Place, primary_key = True)
	serves_hot_dogs = models.BooleanField()
	serves_pizza = models.BooleanField()

	def __unicode__(self):
		return u"%s the restaurant" % self.place.name


class Waiter(models.Model):
	restaurant = models.ForeignKey(Restaurant)
	name = models.CharField(max_length = 50)

	def __unicode__(self):
		return u"%s the waiter at %s" % (self.name, self.restaurant)
