from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):
    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            name="Test Recipe",
            description="Test Description",
            cooking_time=30,
            instructions="Test Instructions"
        )
        self.assertEqual(recipe.name, "Test Recipe")
        self.assertEqual(recipe.description, "Test Description")
        self.assertEqual(recipe.cooking_time, 30)
        self.assertEqual(recipe.instructions, "Test Instructions")