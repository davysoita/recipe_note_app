from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm


def home(request):
    return render(request, "home.html")


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe_list.html", {"recipes": recipes})


def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recipes")
    else:
        form = RecipeForm()
    return render(request, "recipe_form.html", {"form": form})


def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, "recipe_detail.html", {"recipe": recipe})


def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipes")
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "recipe_form.html", {"form": form})


def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == "POST":
        recipe.delete()
        return redirect("recipes")
    return render(request, "recipe_confirm_delete.html", {"recipe": recipe})