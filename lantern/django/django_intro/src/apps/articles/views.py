from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, DetailView, FormView, ListView

from apps.articles.forms import ArticleForm, ArticleImageForm
from apps.articles.models import Article
from django.core import serializers


def main_page(request, some_id=None, *args, **kwargs):
    return render(request, 'pages/main_page.html')


@login_required
def main_page_logged_id(request, some_id=None, *args, **kwargs):
    return render(request, 'pages/main_page.html')


class SearchResultsView(View):
    def get(self, request, **kwargs):
        search_q = request.GET.get('search', '')
        if search_q:
            articles = Article.objects.filter(title__icontains=search_q)
        else:
            articles = Article.objects.all()
        context_data = {
            'articles': articles,
        }
        return render(request, 'pages/search.html', context=context_data)

    def post(self, request):
        return HttpResponse('{}', status=201)


class ShowTitsView(TemplateView):
    template_name = 'articles_list.html'

    def get_context_data(self, **kwargs):
        return {
            'tits': 2
        }


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['tits'] = 42
        return ctx


class ArticleUpdateImageView(FormView):
    form_class = ArticleImageForm
    template_name = 'art-image-update.html'

    def get_success_url(self):
        return reverse('articles:detail', kwargs={'id': self.kwargs['id']})

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['id'] = self.kwargs['id']
        return ctx


def delete_article(request, id):
    obj = get_object_or_404(Article, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/articles/results/")

    return render(request, "delete_article.html")


def article_json(request, id):
    return HttpResponse(serializers.serialize("json", [Article.objects.get(pk=id)]))


def articles_list_json(request):
    return JsonResponse(list(Article.objects.all().values()), safe=False)


class NewArticleFormView(FormView):
    template_name = 'article_form.html'
    form_class = ArticleForm
    success_url = '/articles/post/'


class NewArticleView(FormView):
    template_name = 'new_article.html'
    form_class = ArticleForm
    success_url = '/articles/post/'


class ValidationError(object):
    pass


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx