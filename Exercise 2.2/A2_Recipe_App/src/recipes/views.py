from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from .models import Recipe
from .forms import SignUpForm, SearchForm
import pandas as pd

def home_view(request):
    return render(request, 'recipes/recipes_home.html')

@login_required
def recipes_list(request):
    form = SearchForm(request.GET)
    recipes = Recipe.objects.all()
    
    if form.is_valid():
        name = form.cleaned_data.get('name')
        ingredient = form.cleaned_data.get('ingredient')
        cooking_time = form.cleaned_data.get('cooking_time')
        
        if name:
            recipes = recipes.filter(name__icontains=name)
        if ingredient:
            recipes = recipes.filter(ingredients__icontains=ingredient)
        if cooking_time:
            recipes = recipes.filter(cooking_time=cooking_time)

    # Ensure 'id' is included
    df = pd.DataFrame(list(recipes.values('id', 'name', 'ingredients', 'cooking_time')))
    
    return render(request, 'recipes/recipes_list.html', {
        'form': form,
        'recipes': df.to_dict(orient='records')
    })

@login_required
def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def logout_view(request):
    logout(request)
    return redirect('recipes:logout_success')

def logout_success_view(request):
    return render(request, 'recipes/logout_success.html')

def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipes:home')
    else:
        form = SignUpForm()
    return render(request, 'recipes/register.html', {'form': form})
