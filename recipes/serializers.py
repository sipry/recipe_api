from rest_framework import serializers
from recipes.models import Recipe, Favorites


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'created', 'image',
                  'description', 'ingredients']
        depth = 1


class FavoritesItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ['id', 'user', 'recipe']
