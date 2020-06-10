from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from article.views import ArticleAPIView

urlpatterns = format_suffix_patterns([
    path('article/<int:article_id>', ArticleAPIView.as_view())
])