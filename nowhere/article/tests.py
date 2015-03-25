from django.test import TestCase
from nowhere.article.models import Article
from django.utils import timezone

# Create your tests here.

class ArticleTestCase(TestCase):
	def setUp(self):
		Article.objects.create(title="Test 1", body="blah", pub_date=timezone.now(), likes=0)
	def test_add(self):
		a = Article.objects.get(title="Test 1")
		self.assertEqual(a.body, "blah")
