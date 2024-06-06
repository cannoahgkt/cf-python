# Recipe App: Data Structures in Python

## Exercise 1.2: Exploring Data Types in Python

### Learning Objectives

- Gain proficiency in using variables and data types in Python.
- Understand the concept of objects and their role in Python programming.
- Develop a robust data structure for managing recipes in a Recipe app.

### Lessons Covered

1. **Getting Started with IPython Shell**: Introduction to interactive Python sessions.
2. **Essential Commands and Functions in IPython**: Exploring essential commands and functions.
3. **Understanding Variables and Data Types**: Delving into the concept of variables and various data types in Python.
4. **Exploring Scalar Objects**: Understanding scalar objects and their significance.
5. **Diving into Non-Scalar Objects**: Exploring the world of non-scalar objects and their practical applications.
6. **Mastering Tuples**: Learning about tuples and their characteristics.
7. **Harnessing the Power of Lists**: Understanding lists, a versatile and fundamental data structure.
8. **Manipulating Strings**: Exploring string manipulation techniques and operations.
9. **Unveiling the Magic of Dictionaries**: Introduction to dictionaries and their indispensable role in Python.

### Learning Journal

#### Day 1
- Set up the project folder and created the initial files.
- Decided to use a dictionary for individual recipes and a list for storing all recipes.
- Created the first recipe and added it to the list.

#### Day 2
- Added additional recipes.
- Printed the ingredients of each recipe.
- Documented the data structure justification in the README file.

## Exercise 1.3: Recipe Difficulty Calculator

### Learning Objectives

- Collect multiple recipes from the user and store them in a structured format.
- Maintain a list of unique ingredients across all recipes.
- Calculate and display the difficulty level of each recipe based on certain criteria.
- Organize and present the collected data clearly.

### Overview

In Exercise 1.3, you will enhance your Recipe app by adding functionality to determine and display the difficulty level of each recipe. You'll collect recipes from the user, store them, and then calculate the difficulty based on the number of ingredients and cooking time.

### Steps

1. **Initialize Lists**: Start by initializing two empty lists: `recipes_list` and `ingredients_list`.
2. **Define Function**: Create a function called `take_recipe` to collect recipe details from the user.
3. **Collect Recipes**: Use a loop to collect multiple recipes, updating the `recipes_list` and `ingredients_list`.
4. **Calculate Difficulty**: Determine the difficulty level of each recipe based on the given criteria.
5. **Display Results**: Print each recipe's details along with its difficulty level and the list of all unique ingredients.

### Learning Journal

#### Day 1
- Set up the initial lists and defined the `take_recipe` function.
- Collected user input for recipes and stored them in the list.
- Ensured unique ingredients were tracked across all recipes.

#### Day 2
- Added logic to calculate the difficulty level of each recipe.
- Printed the details of each recipe including its difficulty.
- Displayed the sorted list of all unique ingredients.

## Exercise 1.4: Storing and Searching Recipes

### Learning Objectives

- Store recipes in a binary file using the `pickle` module.
- Retrieve and search recipes based on ingredients.
- Implement robust file handling and user input validation.

### Overview

In this exercise, you will extend your Recipe app to store recipes on your machine and allow searching for recipes by ingredients. This task is divided into two scripts: `recipe_input.py` and `recipe_search.py`.

### Steps

#### Part 1: `recipe_input.py` Script

1. **Import Modules**: Import the `pickle` module.
2. **Define Functions**: 
   - `calc_difficulty()`: Calculates the difficulty of a recipe based on cooking time and the number of ingredients.
   - `take_recipe()`: Takes recipe details from the user and returns a dictionary.
3. **Main Code**:
   - Handle file operations with try-except-else-finally blocks.
   - Collect multiple recipes from the user and update the recipes and ingredients lists.
   - Store the updated data in a binary file.

#### Part 2: `recipe_search.py` Script

1. **Import Modules**: Import the `pickle` module.
2. **Define Functions**: 
   - `display_recipe()`: Displays recipe details.
   - `search_ingredient()`: Searches for recipes containing a specific ingredient.
3. **Main Code**:
   - Handle file operations with try-except-else blocks.
   - Allow the user to search for recipes by ingredients.

### Learning Journal

#### Day 1: Setting Up and Planning

**What I did:**
- Reviewed the task requirements and broke them down into manageable steps.
- Set up the project folder and created two new Python scripts: `recipe_input.py` and `recipe_search.py`.

**Challenges:**
- Understanding the requirements for storing recipes in a binary file.
- Figuring out how to structure the data to make it easy to add and search for recipes.

**What I learned:**
- The importance of planning and breaking down complex tasks into smaller, manageable parts.
- How to handle binary files using the `pickle` module in Python.

#### Day 2: Implementing `recipe_input.py`

**What I did:**
- Implemented the `calc_difficulty` function to determine the difficulty level of a recipe.
- Created the `take_recipe` function to take recipe details from the user and compile them into a dictionary.
- Wrote the main part of the script to handle file operations, read existing data, and append new recipes.

**Challenges:**
- Handling exceptions correctly to ensure the script can create a new file if one doesn't exist.
- Ensuring that ingredients are not duplicated in the `all_ingredients` list.

**What I learned:**
- How to define and use functions to modularize code and make it more readable.
- The use of try-except blocks to handle file operations safely.

#### Day 3: Implementing `recipe_search.py`

**What I did:**
- Created the `display_recipe` function to print recipe details in a readable format.
- Implemented the `search_ingredient` function to allow users to search for recipes by ingredient.
- Wrote the main part of the script to read data from the binary file and search for recipes.

**Challenges:**
- Displaying the list of ingredients and handling user input to select an ingredient.
- Making sure the search function efficiently finds and displays all relevant recipes.

**What I learned:**
- How to use the `enumerate` function to display a list with index numbers.
- The importance of user input validation to prevent errors and improve user experience.

#### Day 4: Testing and Documentation

**What I did:**
- Tested both scripts to ensure they work as expected.
- Entered several sample recipes and verified that they were stored and retrieved correctly.
- Took screenshots of the terminal output at various steps and saved them with appropriate filenames.

**Challenges:**
- Ensuring that the scripts handle edge cases, such as empty input or invalid file names.
- Documenting each step clearly to make it easy to follow the process.

**What I learned:**
- The value of thorough testing to identify and fix issues before final submission.
- How to document the development process effectively, which is crucial for both personal learning and sharing with others.

#### Overall Reflection

**Key takeaways:**
- Working with binary files and the `pickle` module is essential for storing complex data structures in Python.
- Proper error handling and user input validation are critical for creating robust scripts.
- Breaking down tasks into smaller steps and documenting the process helps in managing and completing projects successfully.

**Next steps:**
- Continue to practice working with file operations and data structures in Python.
- Explore other modules and techniques for data storage and retrieval.
- Apply the concepts learned in this task to future projects and exercises.