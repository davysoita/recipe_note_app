from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recipes/", views.recipe_list, name="recipes"),
    path("recipe/add/", views.add_recipe, name="add_recipe"),
    path("recipe/<int:id>/", views.recipe_detail, name="recipe_detail"),
    path("recipe/<int:id>/edit/", views.update_recipe, name="edit_recipe"),
    path("recipe/<int:id>/delete/", views.delete_recipe, name="delete_recipe"),
]