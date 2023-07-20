""""

GROUP A.10
    Create a recipe organizer application that allows users to
    add, view, and search for recipes. Implement classes and methods to
    represent recipes and organize the functionality of the application.

"""

import recipe_organizer_module as recipeMod

organizer = recipeMod.RecipeOrganizer()

while True:
    print("""
    What do you want to do?
    1. Add Recipes
    2. View all Recipes
    3. View a specific Recipe (view)
    4. Search Recipes
    5. Exit
    """)
    user_response = input(">>> ")

    if user_response.strip() == "":
        print("\nChoose an option or type 'exit' to close!")
    # ------------------------------
    elif user_response.isalnum():
        if user_response.lower() == "add recipes" or user_response == str(1):
            print("\nProvide Recipe details")
            recipe_name = input("-- Recipe name: ")
            if recipe_name == "":
                print("There must be a recipe name!")
                continue

            recipe_ingredients = input("-- Recipe ingredients (separate with commas ','): ")
            if recipe_ingredients == "":
                print("There must be at least one ingredient!")
                continue

            recipe_instructions = input("-- Recipe instructions (end each instruction with ';'): ")
            if recipe_instructions == "":
                print("There must be at least one instruction!")
                continue
            else:
                recipe_instructions_list = recipe_instructions.split(';')
            if recipe_name != "" and recipe_ingredients != "" and recipe_instructions != "":
                recipe = recipeMod.Recipe(recipe_name, recipe_ingredients, recipe_instructions_list)
                organizer.add_recipe(recipe)
            else:
                print("The recipe name, recipe ingredients or recipe instructions may have been left empty!")

        elif user_response.lower() == "view all recipes" or user_response == str(2):
            organizer.view_recipes()

        elif user_response.lower() in "view a specific recipe" or user_response == str(3):
            if organizer.recipes is None:
                print("No recipe has been added yet!")
            else:
                print("\nWhat recipe do you want to view?")
                user_input = input(">>> ")
                organizer.view_recipes(user_input)

        elif user_response.lower() == "search recipes" or user_response == str(4):
            print("\nEnter Recipe name")
            search_keyword = input("🔎 ")
            organizer.search_recipe(search_keyword)
        elif user_response.lower() == "exit" or user_response == str(5):
            print("Thank you! \nBye!")
            break
        else:
            print("!! Invalid input !!")
    # ------------------------------
    else:
        print("!! Invalid input !!")
