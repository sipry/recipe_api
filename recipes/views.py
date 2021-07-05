from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from recipes.models import Recipe, Favorites
from recipes.serializers import RecipeSerializer, FavoritesItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'PUT'])
def recipe(request, recipe_pk=None):
    if request.method == 'GET':
        if recipe_pk:
            resp = Recipe.objects.get(id=recipe_pk)
            serializer = RecipeSerializer(resp, many=False)
            return Response(serializer.data)
        else:
            resp = Recipe.objects.all()
            serializer = RecipeSerializer(resp, many=True)
            return Response(serializer.data)
    elif request.method == 'PUT':
        try:
            snippet = Recipe.objects.get(id=recipe_pk)
        except Recipe.DoesNotExist:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        serializer = RecipeSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def favorites(request, favorite_pk):
#     if request.method == 'GET':
#         if favorite_pk:
#             resp = Favorites.objects.get(id=favorite_pk)
#             serializer = FavoritesItemSerializer(resp, many=False)
#             return Response(serializer.data)
#         else:
#             resp = Favorites.objects.filter(list_id=favorite_pk)
#             serializer = FavoritesItemSerializer(resp, many=True)
#             return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = FavoritesItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'PUT':
#         try:
#             snippet = Favorites.objects.get(id=favorite_pk)
#         except Recipe.DoesNotExist:
#             return HttpResponse(status=404)
#         data = JSONParser().parse(request)
#         serializer = FavoritesItemSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         resp = Favorites.objects.get(id=favorite_pk)
#         resp.delete()
#         return HttpResponse(status=204)


