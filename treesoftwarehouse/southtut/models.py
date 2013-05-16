from django.db import models

class Knight(models.Model):
	name = models.CharField(max_length = 80, unique = True)
	of_the_round_table = models.BooleanField()
	dances_whenever_able = models.BooleanField()
	apple = models.SmallIntegerField(null = False)


	def __unicode__(self):
		return "%s %s" % (self.name, self.of_the_round_table)
