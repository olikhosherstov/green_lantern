from django import forms
from django.forms import ModelForm
from apps.articles.models import Article


class SearchForm(forms.Form):
    search = forms.CharField(required=False)


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "body", "tags"]
