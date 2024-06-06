# Recipe Class Definition

class Recipe:
    # Class-level attribute to track all unique ingredients
    unique_ingredients = set()

    def __init__(self, recipe_name, time_to_cook):
        # Initialize recipe with name and cooking time
        self.recipe_name = recipe_name
        self.cooking_time = time_to_cook
        self.recipe_ingredients = []
        self.difficulty_level = None

    def add_ingredients(self, *ingredients):
        # Add ingredients to the recipe
        self.recipe_ingredients.extend(ingredients)
        self.update_unique_ingredients()

    def update_unique_ingredients(self):
        # Update unique ingredients set
        for ingredient in self.recipe_ingredients:
            Recipe.unique_ingredients.add(ingredient)

    def calculate_difficulty(self):
        # Determine the difficulty level of the recipe
        if self.cooking_time < 10:
            if len(self.recipe_ingredients) < 4:
                self.difficulty_level = "Easy"
            else:
                self.difficulty_level = "Medium"
        else:
            if len(self.recipe_ingredients) < 4:
                self.difficulty_level = "Intermediate"
            else:
                self.difficulty_level = "Hard"

    def get_difficulty(self):
        # Retrieve the difficulty level, calculate if not set
        if self.difficulty_level is None:
            self.calculate_difficulty()
        return self.difficulty_level

    def search_for_ingredient(self, ingredient):
        # Check if an ingredient is in the recipe
        return ingredient in self.recipe_ingredients

    def set_name(self, new_name):
        # Set a new name for the recipe
        self.recipe_name = new_name

    def get_name(self):
        # Get the current name of the recipe
        return self.recipe_name

    def set_cooking_time(self, new_cooking_time):
        # Set a new cooking time for the recipe
        self.cooking_time = new_cooking_time

    def get_cooking_time(self):
        # Get the current cooking time of the recipe
        return self.cooking_time

    def get_ingredients(self):
        # Get the list of ingredients for the recipe
        return self.recipe_ingredients

    def __str__(self):
        # Return a formatted string representation of the recipe
        self.calculate_difficulty()
        return f"Recipe: {self.recipe_name}\nIngredients: {', '.join(self.recipe_ingredients)}\nCooking Time: {self.cooking_time} minutes\nDifficulty: {self.difficulty_level}"


# Function to search for recipes by ingredient

def find_recipes_by_ingredient(recipes, ingredient):
    # Search for recipes that include a specific ingredient
    for recipe in recipes:
        if recipe.search_for_ingredient(ingredient):
            print(recipe)


# Main script

# Create recipe instances and add ingredients
tea = Recipe("Tea", 5)
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
print(tea)

coffee = Recipe("Coffee", 5)
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
print(coffee)

cake = Recipe("Cake", 50)
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
print(cake)

banana_smoothie = Recipe("Banana Smoothie", 5)
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
print(banana_smoothie)

# Compile a list of all recipes
all_recipes = [tea, coffee, cake, banana_smoothie]

# Search for recipes by specific ingredients
print("\nRecipes that contain Water:")
find_recipes_by_ingredient(all_recipes, "Water")

print("\nRecipes that contain Sugar:")
find_recipes_by_ingredient(all_recipes, "Sugar")

print("\nRecipes that contain Bananas:")
find_recipes_by_ingredient(all_recipes, "Bananas")
