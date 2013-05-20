from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PollTest(LiveServerTestCase):

	fixtures = ['admin_user.json']
	
	def setUp(self):
#		contador = 0
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	
	def tearDown(self):
		self.browser.quit()
		
	def test_can_create_new_poll_via_admin_site(self):
#		contador +=1
		# Kayle opens he browser and goes to the adimn page
		self.browser.get(self.live_server_url + '/admin/')
		
		# She sees the familiar 'Django Administration' heading
		body = self.browser.find_element_by_tag_name('body')				
		self.assertIn('Django a	dministration', body.text)
		
		# She types in her name and passwords and hints return
		username_field = self.browser.find_element_by_name('username')
		username_field.send_keys('admin')
		
		password_field = self.browser.find_element_by_name('password')
		password_field.send_keys('admin')
		password_field.send_keys(Keys.RETURN)
		
		# Her username and password are accepted, and she is taken to the site Administration Page
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Site administration', body.text)
		
		# Now she sees a couple of hyperlinks thar says "Polls"
		polls_links = self.browser.find_elements_by_link_text('Polls')
		self.assertEquals(len(polls_links), 2)
		
		# TODO: Kayle uses the site to create a poll
		self.fail('TODO: finish all tests!')
'''		
	def test_primeiro(self):
		pass
	
	def test_segundo(self):
		pass
'''		
