from django.contrib.sitemaps.views import index
from django.urls import path

from apps.articles.views import main_page, \
    SearchResultsView, ArticleListView, \
    main_page_logged_id, article_json, \
    articles_list_json, NewArticleFormView

app_name = "articles"

urlpatterns = [
    path("", index, name="index"),
    path("search/", main_page_logged_id, name="main-page"),
    path("results/", SearchResultsView.as_view(), name="search-results"),
    path("json/", article_json, name="json-article-list"),
    path("json_list/", articles_list_json, name="json-article-list"),
    path("list/", ArticleListView.as_view(), name="article-list"),
    path("form/", NewArticleFormView.as_view(), name="article-form"),
]