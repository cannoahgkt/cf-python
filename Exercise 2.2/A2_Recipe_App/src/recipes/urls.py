from django.urls import path
from .views import home_view, recipes_list, recipe_detail

app_name = 'recipes'

urlpatterns = [
    path('', home_view, name='home'),
    path('recipes/', recipes_list, name='recipes_list'),
    path('recipes/<int:id>/', recipe_detail, name='recipe_detail'),
]
