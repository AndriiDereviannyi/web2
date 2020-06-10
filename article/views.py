from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from article.models import Article


# Create your views here.

class ArticleAPIView(APIView):
    def get(self, article_id):
        # zminna = Article.object.filter(id = article_id).first()
        # if zminna:
        #   return JsonResponse({"title":zminna.title})
        return JsonResponse({"title": "sometext"}, status=200)