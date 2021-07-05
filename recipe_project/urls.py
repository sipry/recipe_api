from django.contrib import admin
from django.urls import path
from recipes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', views.recipe),
    path('recipes/<int:recipe_pk>/', views.recipe),
    # path('recipes/<int:favorite_pk>/', views.favorites),
]
