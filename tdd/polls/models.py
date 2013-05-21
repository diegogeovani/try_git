from django.db import models

class Poll(models.Model):
	question =  models.CharField(max_length = 150, null=True, blank=True)
	pub_date =  models.DateTimeField(null=True, blank=True, verbose_name = 'Date published')	
	
	def __unicode__(self):
		return self.question
		

class Choice(models.Model):
	choice = models.CharField(max_length = '100')
	votes = models.IntegerField(default = 0)
	poll = models.ForeignKey(Poll)
