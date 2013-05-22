from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import namedtuple

PollInfo = namedtuple('PollInfo', ['question', 'choices'])
POLL1 = PollInfo(
	question = 'How awesome is TDD?',
	choices = [
		'truly awesome',
		'moderately awesome',
		'not awesome at all',
	],
)

POLL2 = PollInfo(
	question = "What's the most efficient development framework?'",
	choices = [
		'Django',
		'Ruby on Rails',
		'Spring',
	],
)
class PollTest(LiveServerTestCase):

	fixtures = ['admin_user.json']
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	
	def tearDown(self):
		self.browser.quit()
		
	def test_can_create_new_poll_via_admin_site(self):
	
		# Kayle opens he browser and goes to the adimn page
		self.browser.get(self.live_server_url + '/admin/')
		
		# She sees the familiar 'Django Administration' heading
		body = self.browser.find_element_by_tag_name('body')				
		self.assertIn('Django administration', body.text)
		
		# She types in her name and passwords and hints return
		username_field = self.browser.find_element_by_name('username')
		username_field.send_keys('diego')
		
		password_field = self.browser.find_element_by_name('password')
		password_field.send_keys('kml9055')
		password_field.send_keys(Keys.RETURN)
		
		# Her username and password are accepted, and she is taken to the site Administration Page
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Site administration', body.text)
		
		# Now she sees a couple of hyperlinks thar says "Polls"
		polls_links = self.browser.find_elements_by_link_text('Polls')
		self.assertEquals(len(polls_links), 2)
		
		# Kayle clicks in the second one
		polls_links[1].click()
		
		# She sees there are no polls listed
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('0 polls', body.text)
		
		# She clicks in 'add' to create a poll
		new_poll_link = self.browser.find_element_by_link_text('Add poll')	
		new_poll_link.click() 
		
		# She sees some input fields
		body = self.browser.find_element_by_tag_name('body')	
		self.assertIn('Question:', body.text)
		self.assertIn('Date published:', body.text)
		
		# She types a question
		question_field = self.browser.find_element_by_name('question')
		question_field.send_keys('How awesome is TDD?')
		
		# She types the date
		date_field = self.browser.find_element_by_name('pub_date_0')
		date_field.send_keys('01/01/12')
		time_field = self.browser.find_element_by_name('pub_date_1')		
		time_field.send_keys('00:00')
		
		# She adds choices for the poll
		choice_1 = self.browser.find_element_by_name('choice_set-0-choice')
		choice_1.send_keys('truly awesome')
		choice_2 = self.browser.find_element_by_name('choice_set-1-choice')
		choice_2.send_keys('moderately awesome')		
		choice_3 = self.browser.find_element_by_name('choice_set-2-choice')				
		choice_3.send_keys('Not awesome at all')		
		
		# She clicks in the 'save' button
		save_button = self.browser.find_element_by_css_selector("input[value='Save']")
		save_button.click()
		
		# She sees the result
		new_poll_links = self.browser.find_elements_by_link_text('How awesome is TDD?')
		self.assertEquals(len(new_poll_links), 1)
		
		# She's happy now! ;)'
		
		# TODO: Kayle uses the site to create a poll
		# self.fail('TODO: finish all tests!')
	
	def _setup_polls_via_admin(self):
	
		# Kayle logs into the site
		self.browser.get(self.live_server_url + '/admin/')
		body = self.browser.find_element_by_tag_name('body')				
		self.assertIn('Django administration', body.text)
		username_field = self.browser.find_element_by_name('username')
		username_field.send_keys('diego')		
		password_field = self.browser.find_element_by_name('password')
		password_field.send_keys('kml9055')
		password_field.send_keys(Keys.RETURN)
		
		# She sees a number of polls to enter
		for poll_info in [POLL1, POLL2]:		
			# She follows the chosen link
			self.browser.find_elements_by_link_text('Polls')[1].click()
			self.browser.find_element_by_link_text('Add poll').click()
			
			# She sets question and date
			question_field = self.browser.find_element_by_name('question')
			question_field.send_keys(poll_info.question)
			self.browser.find_element_by_link_text('Today').click()
			self.browser.find_element_by_link_text('Now').click()
			# She enters choices for the poll
			for i, choice_text in enumerate(poll_info.choices):
				choice_field = self.browser.find_element_by_name('choice_set-%d-choice' % i)
				choice_field.send_keys(choice_text)
			
			# She saves the poll
			save_button = self.browser.find_element_by_css_selector("input[value = 'Save']")
			save_button.click()
			
			# She sees her poll listed
			new_poll_links = self.browser.find_elements_by_link_text(poll_info.question)
			self.assertEquals(len(new_poll_links), 1)
			
			# She goes back to the root
			self.browser.get(self.live_server_url + '/admin/')
			
			# She logs out of the site
		self.browser.find_element_by_link_text('Log out').click()
	
	
	def test_regular_user_voting_on_a_new_poll(self):
	
		self._setup_polls_via_admin()
		
		# Brand, a regular user, sees a list of polls
		self.browser.get(self.live_server_url)
		heading = self.browser.find_element_by_tag_name('h1')
		self.assertEquals(heading.text, 'Polls')
		
		# Brand clicks on the first link
		first_poll_title = POLL1.question
		self.browser.find_element_by_link_text(first_poll_title).click()
		
		# He sees 'results' page
		main_heading = self.browser.find_element_by_tag_name('h1')
		self.assertEquals(main_heading.text, 'Polls Results')
		sub_heading = self.browser.find_element_by_tag_name('h2')
		self.assertEquals(sub_heading.text, first_poll_title)		
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('No one has voted yet...', body.text)		
		
		#TODO
		self.fail('TODO')
