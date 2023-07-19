import recipe_organizer_module as recipeMod

organizer = recipeMod.RecipeOrganizer()

while True:
    print("""
    What do you want to do?
    1. Add Recipes
    2. View all Recipes
    3. View a specific Recipe
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
            recipe_ingredients = input("-- Recipe ingredients: ")
            recipe_instructions = input("-- Recipe instructions (end each instruction with ';'): ")
            recipe_instructions_list = recipe_instructions.split(';')
            recipe = recipeMod.Recipe(recipe_name, recipe_ingredients, recipe_instructions_list)
            organizer.add_recipe(recipe)

        elif user_response.lower() == "view all recipes" or user_response == str(2):
            organizer.view_recipes()

        elif user_response == "view a specific recipe" or user_response == str(3):
            if organizer.recipes is None:
                print("No recipe has been added yet!")
            else:
                print("\nWhat recipe do you want to view?")
                user_input = input(">>> ")
                organizer.view_recipes(user_input)

        elif user_response.lower() == "search recipes" or user_response == str(4):
            print("\nEnter Recipe name or Recipe ingredient")
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
