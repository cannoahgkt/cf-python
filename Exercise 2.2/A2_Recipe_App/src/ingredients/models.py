from django.db import models
from recipes.models import Recipe

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return self.name
