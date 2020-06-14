from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView

from apps.articles.forms import ArticleForm
from apps.articles.models import Article


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


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['tits'] = 42
        return ctx


def article_json(request, id):
    return HttpResponse(serializers.serialize("json", [Article.objects.get(pk=id)]))


def articles_list_json(request):
    return JsonResponse(list(Article.objects.all().values()), safe=False)


class ArticleCreate(CreateView):
    model = Article
    fields = ['title', 'body', 'tags']
    success_url = reverse_lazy('success_url')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super(ArticleCreate, self).form_valid(form)


class ArticleUpdate(UpdateView):
    model = Article
    fields = ['title', 'body', 'tags']
    success_url = reverse_lazy('success_url')


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('success_url')


class ValidationError(object):
    pass


class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx
