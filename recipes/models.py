from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=250, null=True)
    description = models.TextField()
    ingredients = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Favorites(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
