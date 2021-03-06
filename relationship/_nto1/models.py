from django.db import models


class Reporter(models.Model):
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	email = models.EmailField()

	def __unicode__(self):
		return u"%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
	headline = models.CharField(max_length = 100)
	pub_date = models.DateField('date published')
	reporter = models.ForeignKey(Reporter, related_name = 'articles')

	def __unicode__(self):
		return u"%s %s" % (self.headline, self.pub_date)

	class Meta:
		ordering = ('headline',)
