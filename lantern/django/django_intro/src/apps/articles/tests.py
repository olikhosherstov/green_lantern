from django.test import TestCase

# Create your tests here.
from django.utils.baseconv import base64

from apps.articles.models import Article, Tag
from apps.articles.forms import ArticleForm
from django.test import Client


#Model testing
class ArticleModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Article.objects.create(title='something',
                               body='something about something')

    def test_fields_label(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')
        field_label = article._meta.get_field('body').verbose_name
        self.assertEquals(field_label, 'body')

    def test_title_max_length(self):
        article = Article.objects.get(id=1)
        max_length = article._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_body_max_length(self):
        article = Article.objects.get(id=1)
        max_length = article._meta.get_field('body').max_length
        print("Max length")
        print(max_length)
        self.assertEquals(max_length, 5000)


#Form testing
class ArticleFormTest(TestCase):
    @classmethod
    def setUp(cls):
        Article.objects.create(title='something',
                               body='something about something')

    def test_form_label(self):
        form = ArticleForm()
        self.assertTrue(form.fields["title"].label == 'Title')
        self.assertTrue(form.fields["body"].label == 'Body')

    def test_form_valid(self):
        form_data = {'title': Article.title,
                     'body': Article.body}
        form = ArticleForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = ArticleForm(data={'title': "", 'body': ""})
        self.assertFalse(form.is_valid())
