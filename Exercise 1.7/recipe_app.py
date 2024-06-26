import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define your database credentials
username = 'cf-python'
password = 'password'
hostname = 'localhost'
database_name = 'task_database'

# Create the engine
engine = db.create_engine(f'mysql+pymysql://{username}:{password}@{hostname}/{database_name}')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Declare a base
Base = declarative_base()

# Define the Recipe model
class Recipe(Base):
    __tablename__ = 'final_recipes'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    cooking_time = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Recipe(id={self.id}, name={self.name}, difficulty={self.difficulty})"
    
    def __str__(self):
        ingredients_list = self.return_ingredients_as_list()
        ingredients_str = "\n".join(f"\t{ingredient}" for ingredient in ingredients_list)
        return (
            f"\nRecipe ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Ingredients:\n{ingredients_str}\n"
            f"Cooking Time (mins): {self.cooking_time}\n"
            f"Difficulty: {self.difficulty}\n"
            f"{'-'*40}\n"
        )
    
    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.return_ingredients_as_list()) < 4:
            self.difficulty = 'Easy'
        elif self.cooking_time < 10 and len(self.return_ingredients_as_list()) >= 4:
            self.difficulty = 'Medium'
        elif self.cooking_time >= 10 and len(self.return_ingredients_as_list()) < 4:
            self.difficulty = 'Intermediate'
        else:
            self.difficulty = 'Hard'
    
    def return_ingredients_as_list(self):
        if self.ingredients:
            return self.ingredients.split(", ")
        return []

# Create the table
Base.metadata.create_all(engine)

def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"

def insert_recipe(name, ingredients, cooking_time):
    difficulty = calculate_difficulty(cooking_time, ingredients)
    ingredients_str = ", ".join(ingredients)
    new_recipe = Recipe(name=name, ingredients=ingredients_str, cooking_time=cooking_time, difficulty=difficulty)
    session.add(new_recipe)
    session.commit()
    print("Recipe added successfully!")

def create_recipe():
    name = input("Enter the recipe name (max 50 characters): ")
    if len(name) > 50 or not name.isalnum():
        print("Invalid recipe name.")
        return

    try:
        cooking_time = int(input("Enter the cooking time in minutes: "))
    except ValueError:
        print("Invalid cooking time. Must be an integer.")
        return

    ingredients = input("Enter the ingredients (separated by commas): ").split(", ")
    
    insert_recipe(name, ingredients, cooking_time)

def view_all_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found in the database.")
        return

    for recipe in recipes:
        print(recipe)

def search_by_ingredients():
    all_ingredients = set()
    results = session.query(Recipe.ingredients).all()
    for result in results:
        ingredients_list = result[0].split(", ")
        all_ingredients.update(ingredients_list)

    all_ingredients = list(all_ingredients)
    for idx, ingredient in enumerate(all_ingredients, start=1):
        print(f"{idx}. {ingredient}")
    
    selected_indices = input("Enter the numbers of the ingredients to search for, separated by spaces: ").split()
    try:
        selected_ingredients = [all_ingredients[int(index) - 1] for index in selected_indices]
    except (IndexError, ValueError):
        print("Invalid selection.")
        return

    conditions = [Recipe.ingredients.like(f"%{ingredient}%") for ingredient in selected_ingredients]
    results = session.query(Recipe).filter(db.or_(*conditions)).all()

    if results:
        for recipe in results:
            print(recipe)
    else:
        print("No recipes match the selected ingredients.")

def edit_recipe():
    recipes = session.query(Recipe).all()
    for recipe in recipes:
        print(f"{recipe.id}. {recipe.name}")
    
    try:
        recipe_id = int(input("Enter the ID of the recipe to edit: "))
        recipe_to_edit = session.query(Recipe).filter_by(id=recipe_id).one()
    except (ValueError, db.orm.exc.NoResultFound):
        print("Invalid recipe ID.")
        return

    print(f"1. Name: {recipe_to_edit.name}")
    print(f"2. Ingredients: {recipe_to_edit.ingredients}")
    print(f"3. Cooking Time: {recipe_to_edit.cooking_time}")
    
    attribute_to_edit = input("Enter the number of the attribute you want to edit: ")
    
    if attribute_to_edit == '1':
        new_name = input("Enter the new name: ")
        if len(new_name) > 50 or not new_name.isalnum():
            print("Invalid name.")
        else:
            recipe_to_edit.name = new_name
    elif attribute_to_edit == '2':
        ingredients = input("Enter the ingredients (separated by commas): ").split(", ")
        recipe_to_edit.ingredients = ", ".join(ingredients)
    elif attribute_to_edit == '3':
        try:
            new_cooking_time = int(input("Enter the new cooking time: "))
            recipe_to_edit.cooking_time = new_cooking_time
        except ValueError:
            print("Invalid cooking time.")
            return
    else:
        print("Invalid selection.")
        return
    
    recipe_to_edit.calculate_difficulty()
    session.commit()
    print("Recipe updated successfully!")

def delete_recipe():
    recipes = session.query(Recipe).all()
    for recipe in recipes:
        print(f"{recipe.id}. {recipe.name}")
    
    try:
        recipe_id = int(input("Enter the ID of the recipe to delete: "))
        recipe_to_delete = session.query(Recipe).filter_by(id=recipe_id).one()
    except (ValueError, db.orm.exc.NoResultFound):
        print("Invalid recipe ID.")
        return

    confirm = input(f"Are you sure you want to delete the recipe '{recipe_to_delete.name}'? (yes/no): ").lower()
    if confirm == 'yes':
        session.delete(recipe_to_delete)
        session.commit()
        print("Recipe deleted successfully!")
    else:
        print("Deletion cancelled.")

def main_menu():
    while True:
        print("\nRecipe App Main Menu")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredients")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("Type 'quit' to exit the application.")
        
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_all_recipes()
        elif choice == '3':
            search_by_ingredients()
        elif choice == '4':
            edit_recipe()
        elif choice == '5':
            delete_recipe()
        elif choice == 'quit':
            session.close()
            engine.dispose()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
