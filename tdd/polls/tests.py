from django.test import TestCase
from django.utils import timezone
from polls.models import Poll, Choice


class PollModelTest(TestCase):

	def test_creating_a_new_poll_and_saving_it_to_the_database(self):		
	
		# Every test creates a poll
		poll = Poll()
		poll.question = "What's your favorite programming language?"
		self.assertEquals(unicode(poll), poll.question)
		poll.pub_date = timezone.now()		
		
		# We can save the object into the database
		poll.save()
		
		# Creating a poll-choice relationship 
		choice = Choice()
		self.assertEquals(choice.votes, 0)
		choice.poll = poll
		
		# A choice
		choice.choice = 'fucking awesome'
		choice.votes = 5
		choice.save()
		
		# reverse lookup
		poll_choices = poll.choice_set.all()
		self.assertEquals(poll_choices.count(), 1)
				
		# Are they saved?
		all_polls_in_database = Poll.objects.all()
		self.assertEquals(len(all_polls_in_database), 1)
		only_poll_in_database = all_polls_in_database[0]
		self.assertEquals(only_poll_in_database, poll)
		
		choice_from_db = poll_choices[0]
		self.assertEquals(choice_from_db, choice)
		self.assertEquals(choice_from_db.choice, choice.choice)
		self.assertEquals(choice_from_db.votes, choice.votes)				
				
		# Checking its attributes content
		self.assertEquals(only_poll_in_database.question, "What's your favorite programming language?")
		self.assertEquals(only_poll_in_database.pub_date, poll.pub_date)		
		
	def test_verbose_name_for_pub_date(self):
	
		for field in Poll._meta.fields:
			if field.name == 'pub_date':
				self.assertEquals(field.verbose_name, 'Date published')
				
	
class HomePageViewTest(TestCase):
	
	def test_root_url_shows_all_polls(self):
		# There are two polls
		poll1 = Poll(question = "Whats your favorite social network?", pub_date = timezone.now())
		poll2 = Poll(question = "How is it going?", pub_date = timezone.now())		
		
		poll1.save()
		poll2.save()		
		
		response = self.client.get('/')

		# Am I using the right template?
		self.assertTemplateUsed(response, 'home.html')				
		
		# Were the polls sent to the template?
		polls_in_context = response.context['polls']
		self.assertEquals(list(polls_in_context), [poll1, poll2])
		
		# Are the polls there?
		self.assertIn(poll1.question, response.content)
		self.assertIn(poll2.question, response.content)		
		
