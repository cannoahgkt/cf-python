from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cooking_time = models.IntegerField()
    instructions = models.TextField()  # Add this field

    def __str__(self):
        return self.name
