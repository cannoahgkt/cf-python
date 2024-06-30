from django.test import TestCase
from .models import Recipe, Ingredient

class RecipeTestCase(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            name='Test Recipe',
            description='A test recipe description.',
            cooking_time=30,
            instructions='Test instructions.'
        )
        Ingredient.objects.create(
            name='Test Ingredient',
            quantity=1,
            unit='unit',
            recipe=self.recipe
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.name, 'Test Recipe')

    def test_recipe_detail_view(self):
        response = self.client.get(f'/recipes/{self.recipe.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')

    def test_recipes_list_view(self):
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')