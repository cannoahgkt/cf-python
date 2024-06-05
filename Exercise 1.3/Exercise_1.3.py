# Initialize empty lists
recipes_list = []
ingredients_list = []

def take_recipe():
    # Get user input for recipe details
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time in minutes: "))
    
    # Get ingredients as a comma-separated string and convert to a list
    ingredients = input("Enter the ingredients (comma-separated): ").split(",")
    ingredients = [ingredient.strip() for ingredient in ingredients]
    
    # Create a dictionary to store the recipe
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    
    return recipe

def main():
    n = int(input("How many recipes would you like to enter? "))
    
    for _ in range(n):
        recipe = take_recipe()
        
        # Add unique ingredients to ingredients_list
        for ingredient in recipe['ingredients']:
            if ingredient not in ingredients_list:
                ingredients_list.append(ingredient)
        
        # Add the recipe to recipes_list
        recipes_list.append(recipe)
    
    # Display all recipes and their difficulty levels
    for recipe in recipes_list:
        name = recipe['name']
        cooking_time = recipe['cooking_time']
        ingredients = recipe['ingredients']
        
        # Determine the difficulty level
        if cooking_time < 10:
            if len(ingredients) < 4:
                difficulty = "Easy"
            else:
                difficulty = "Medium"
        else:
            if len(ingredients) < 4:
                difficulty = "Intermediate"
            else:
                difficulty = "Hard"
        
        # Print recipe details
        print(f"\nRecipe: {name}")
        print(f"Cooking Time (min): {cooking_time}")
        print(f"Ingredients: {', '.join(ingredients)}")
        print(f"Difficulty Level: {difficulty}")
    
    # Display all unique ingredients in alphabetical order
    print("\nAll ingredients used so far:")
    for ingredient in sorted(ingredients_list):
        print(ingredient)

# Run the main function
if __name__ == "__main__":
    main()