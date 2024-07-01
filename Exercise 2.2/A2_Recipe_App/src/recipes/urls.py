from django.urls import path
from django.views.generic import TemplateView
from recipes.views import home_view, logout_view, recipes_list, recipe_detail, register_view
from django.contrib.auth import views as auth_views

app_name = 'recipes'

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='recipes/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('logout_success/', TemplateView.as_view(template_name='recipes/logout_success.html'), name='logout_success'),
    path('recipes/', recipes_list, name='recipes_list'),
    path('recipes/<int:id>/', recipe_detail, name='recipe_detail'),
    path('register/', register_view, name='register'),
]
