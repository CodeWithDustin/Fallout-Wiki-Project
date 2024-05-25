from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=20, default='Default Game Name')

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField(max_length=500)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name