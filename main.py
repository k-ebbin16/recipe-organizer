class Recipe:
    def __init__(self, recipe_name, ingredients, instructions):
        self.recipe_name = recipe_name.lower()
        self.ingredients = ingredients
        self.ingredients_list = self.ingredients.split(', ')
        self.instructions = instructions

    def display_recipe(self, recipe_name):
        if recipe_name == self.recipe_name:
            print(f"\nRecipe: {self.recipe_name.title()}")
            print(f"Ingredients: {', '.join(self.ingredients_list)}")
            print("<<<Ingredients>>>")
            for n, instructions in dict(enumerate(self.instructions, start=1)).items():
                print(f"{n}. {instructions}")


class RecipeOrganizer:

    def __init__(self):
        self.recipes = None
        self.recipe_list = []
        self.recipe_name_list = []

    def add_recipe(self, recipe):
        if recipe not in self.recipe_list:
            self.recipe_list.append(recipe)
            self.recipe_name_list.append(recipe.recipe_name)
            self.recipes = dict(enumerate(self.recipe_list, start=1))
            print(f"Recipe: '{recipe.recipe_name.title()}' successfully added!")
        else:
            print(f"Recipe: '{recipe.recipe_name.title()}' has already been added!")

    def view_recipes(self, recipe_name=None):
        if recipe_name is None:
            print('\n--- Recipe List ---')
            for n, recipe in self.recipes.items():
                print(f"{n}. {recipe.recipe_name.title()}")
        else:
            recipe_name = recipe_name.lower()
            for recipe in self.recipe_list:
                if recipe_name == recipe.recipe_name:
                    Recipe.display_recipe(recipe, recipe.recipe_name)

    def search_recipe(self, keyword):
        global matching_recipe_list
        matching_recipe = []
        for recipe in self.recipe_list:
            if keyword.lower() in recipe.recipe_name:
                matching_recipe.append(recipe.recipe_name)
                matching_recipe_list = list(enumerate(matching_recipe, start=1))
        if not matching_recipe:
            print("\nNo matching recipes found!")
        else:
            print(f"\n-- {len(matching_recipe)} recipe(s) found!")
            for n, recipe in matching_recipe_list:
                print(f"{n}. {recipe.title()}")


recipe1 = Recipe("Fish Soup", "Fish, Water, Salt", ["Instructions are good"])
organizer = RecipeOrganizer()
organizer.add_recipe(recipe1)
organizer.add_recipe(Recipe("Meat Soup", "Meat, Water, Salt", ["Instructions are good"]))
organizer.add_recipe(Recipe("Fufu", "Meat, Water, Salt", ["Instructions are good"]))
organizer.view_recipes()
organizer.search_recipe("SOUP")

#
# while True:
#     print("""
#     What do you want to do?
#     1. View Recipes
#     2. Add Recipes
#     3. Search Recipes
#     """)
#     user_response = input(">>> ")
#
#     if user_response == "View Recipes" or int(user_response) == 1:
#         RecipeOrganizer.view_recipes("")
