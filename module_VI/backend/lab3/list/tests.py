from django.test import TestCase
from list.models import Category, Item
from datetime import datetime

class TestCidei(TestCase):
	def setUp(self):
		self.cat_one = Category.objects.create(name="Hardware", slug="hardware")
		self.item_one = Item.objects.create(listing="t", name="Computers", category=self.cat_one, department="Electronics", description="lalalala")
		self.item_two = Item.objects.create(listing="p", name="Servers", category=self.cat_one, department="Electronics",description="lololol")

	def test_cat_one(self):
		response = self.client.get('/category/%s/' % self.cat_one.id)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Hardware')





