from django import forms

from apps.articles.models import Article


class SearchForm(forms.Form):
    search = forms.CharField(required=False)


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=255)
    body = forms.CharField(widget=forms.Textarea, label='Body', required=False)


class ArticleImageForm(forms.Form):
    image = forms.ImageField(required=False)


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "body"]