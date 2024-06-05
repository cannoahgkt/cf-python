# Step 1: Create recipe_1
recipe_1 = {
    "name": "Tea",
    "cooking_time": 5,
    "ingredients": ["Tea leaves", "Sugar", "Water"]
}

# Step 2: Create all_recipes and add recipe_1
all_recipes = [recipe_1]

# Step 3: Create additional recipes
recipe_2 = {
    "name": "Coffee",
    "cooking_time": 10,
    "ingredients": ["Coffee beans", "Water", "Milk", "Sugar"]
}

recipe_3 = {
    "name": "Pancakes",
    "cooking_time": 20,
    "ingredients": ["Flour", "Eggs", "Milk", "Sugar", "Baking powder"]
}

recipe_4 = {
    "name": "Omelette",
    "cooking_time": 15,
    "ingredients": ["Eggs", "Salt", "Pepper", "Oil", "Cheese"]
}

recipe_5 = {
    "name": "Salad",
    "cooking_time": 10,
    "ingredients": ["Lettuce", "Tomato", "Cucumber", "Olive oil", "Salt"]
}

# Add recipes to all_recipes
all_recipes.extend([recipe_2, recipe_3, recipe_4, recipe_5])

# Step 4: Print ingredients
for recipe in all_recipes:
    print(recipe["ingredients"])
