from django.db import models

from user.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)