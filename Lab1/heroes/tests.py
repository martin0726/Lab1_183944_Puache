from django.test import TestCase


class heroesTest(TestCase):

	def test_heroes_link_returns_correct_html(self):
		response = self.client.get('/heroes')
		self.assertTemplateUsed(response, 'heroes.html')


class heroCloudTest(TestCase):

	def test_hero_cloud_page_returns_correct_html(self):
		response = self.client.get('/heroes/cloud')
		self.assertTemplateUsed(response, 'detail_cloud.html')


class heroSunfloweyTest(TestCase):

	def test_hero_sunflowey_page_returns_correct_html(self):
		response = self.client.get('/heroes/sunflowey')
		self.assertTemplateUsed(response, 'detail_sunflowey.html')


class heroJesterTest(TestCase):

	def test_hero_jester_page_returns_correct_html(self):
		response = self.client.get('/heroes/jester')
		self.assertTemplateUsed(response, 'detail_jester.html')# Create your tests here.
