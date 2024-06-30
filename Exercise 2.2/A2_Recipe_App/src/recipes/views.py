from django.shortcuts import render, get_object_or_404
from .models import Recipe

def home_view(request):
    return render(request, 'recipes/recipes_home.html')

def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipes_list.html', {'recipes': recipes})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
