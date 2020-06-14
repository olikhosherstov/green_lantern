from django.conf.urls import url
from django.contrib.sitemaps.views import index
from django.urls import path
from django.views.generic import TemplateView

from apps.articles.views import main_page, \
    SearchResultsView, ArticleListView, \
    main_page_logged_id, article_json, \
    articles_list_json, ArticleCreate, ArticleUpdate, ArticleDelete

app_name = "articles"

urlpatterns = [
    path("search/", main_page_logged_id, name="main-page"),
    path("results/", SearchResultsView.as_view(), name="search-results"),
    path("json/<int:id>", article_json, name="json-article"),
    path("json_list/", articles_list_json, name="json-article-list"),
    path("article-list/", ArticleListView.as_view(), name="article-list"),
    path("add/", ArticleCreate.as_view(), name='article_add'),
    path("<int:pk>/update/", ArticleUpdate.as_view(), name='article_update'),
    url(r'(?P<pk>\d+)/delete/$', ArticleDelete.as_view(), name='article_delete'),
]
