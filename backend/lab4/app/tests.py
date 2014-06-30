from django.test import TestCase
from app.models import Category, Item
from datetime import datetime
# Create your tests here. import dateTime

class TestCidei(TestCase):
	
	def setUp(self):
		self.cat_one = Category.objects.create(name='Hardware', slug='hardware')
		self.item_one = Item.objects.create(listing='t', name='Computers', category=self.cat_one, department='Electronics', description='lalalsalkfkaj', update_item = datetime.now())
		self.item_two = Item.objects.create(listing='p', name='Server', category=self.cat_one, department='Electronics', description='/lalalsalkfksfs>', update_item = datetime.now())

	def tesdt_cat_one(self):
		response = self.client.get('/categorias/%s/' % self.cat_one.id)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Hardware')

	