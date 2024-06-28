from django.test import TestCase
from recipes.models import Recipe

class IngredientModelTest(TestCase):
    def test_ingredient_creation(self):
        recipe = Recipe.objects.create(
            name="Test Recipe",
            description="A test recipe description",
            cooking_time=30,
            instructions="Test instructions"  # Providing instructions
        )
        self.assertEqual(recipe.name, "Test Recipe")