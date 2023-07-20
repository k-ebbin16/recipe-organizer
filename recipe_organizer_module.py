class Recipe:
    def __init__(self, recipe_name, ingredients, instructions):
        self.recipe_name = recipe_name.lower()
        self.ingredients = ingredients.title()
        self.ingredients_list = self.ingredients.split(',')
        self.instructions = instructions

    def display_recipe(self, recipe_name):
        if recipe_name == self.recipe_name:
            print(f"\nRecipe: {self.recipe_name.title()}")
            print(f"Ingredients: {', '.join(self.ingredients_list)}" if self.ingredients_list is not None else None)
            print("<<< Instructions >>>")
            for n, instruction in dict(enumerate(self.instructions, start=1)).items():
                if instruction.istitle():
                    print(f"{n}. {instruction.strip()}")
                else:
                    print(f"{n}. {instruction.strip().capitalize()}")


class RecipeOrganizer:
    def __init__(self):
        self.recipes = None
        self.recipe_list = []
        self.recipe_name_list = []

    def add_recipe(self, recipe):
        if recipe not in self.recipe_list and recipe.recipe_name not in self.recipe_name_list:
            self.recipe_list.append(recipe)
            self.recipe_name_list.append(recipe.recipe_name)
            self.recipes = dict(enumerate(self.recipe_list, start=1))
            print(f"\nRecipe: '{recipe.recipe_name.title()}' successfully added!")
        else:
            print(f"\nRecipe: '{recipe.recipe_name.title()}' has already been added!")

    def view_recipes(self, recipe_name_to_view=None):
        if recipe_name_to_view is None:
            print('\n--- Recipe List ---')
            try:
                for n, r in self.recipes.items():
                    print(f"{n}. {r.recipe_name.title()}")
            except AttributeError:
                print("No recipe has been added yet!")
        else:
            for r in self.recipe_list:
                if recipe_name_to_view.lower() == r.recipe_name:
                    Recipe.display_recipe(r, r.recipe_name)
                    break
                else:
                    continue
            else:
                print(f"'{recipe_name_to_view}' not found! \n'{recipe_name_to_view}' may not be in recipe list or "
                      f"is spelt wrongly!")

    def search_recipe(self, keyword):
        global matching_recipe_list
        matching_recipe = []
        if not self.recipe_list:
            print("\nNo recipe has been added yet!")
        else:
            for r in self.recipe_list:
                if keyword.lower() in r.recipe_name:
                    matching_recipe.append(r.recipe_name)
                    matching_recipe_list = list(enumerate(matching_recipe, start=1))
            if not matching_recipe:
                print("\nNo matching recipes found!")
            else:
                print(f"\n-- {len(matching_recipe)} recipe(s) found!")
                for n, r in matching_recipe_list:
                    print(f"{n}. {r.title()}")
