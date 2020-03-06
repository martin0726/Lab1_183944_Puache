from django.test import TestCase


class heroesTest(TestCase):

	def test_heroes_link_returns_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')


class heroCloudTest(TestCase):

	def test_hero_cloud_page_returns_correct_html(self):
		response = self.client.get('/tasks')
		self.assertTemplateUsed(response, 'task_list.html')


class heroSunflowey(TestCase):

	def test_hero_sunflowey_page_returns_correct_html(self):
		response = self.client.get('/tasks/new')
		self.assertTemplateUsed(response, 'task_create_form.html')

class heroJester(TestCase):

	def test_hero_jester_page_returns_correct_html(self):
		response = self.client.get('/tasks/new')
		self.assertTemplateUsed(response, 'task_create_form.html')# Create your tests here.
