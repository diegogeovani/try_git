from django.test import TestCase
from django.utils import timezone
from polls.models import Poll

class PollModelTest(TestCase):

	def test_creating_a_new_poll_and_saving_it_to_the_database(self):
		# Create a new Poll object
		poll = Poll(question = "What's your favorite programming language?", pub_date = timezone.timezone.now())
		
		# We can save the object into the database
		poll.save()
		
		# Trying to find the object
		all_polls_in_database = Poll.objects.all()
		self.assertEquals(all_polls_in_database, 1)
		only_poll_in_database = all_polls_in_database[0]
		self.assertEquals(only_poll_in_database, poll)
		
		# Checking its attributes content
		self.assertEquals(only_poll_in_database.question, "What's your favorite programming language?")
		self.assertEquals(only_poll_in_database.pub_date, poll.pub_date)
