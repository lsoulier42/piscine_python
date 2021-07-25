import datetime

class Book:
    def __init__(self, name):
        if self.__check_name(name):
            self.name = name
            self.last_update = datetime.datetime.now()
            self.creation_date = datetime.datetime.now()
            self.recipes_list = []
        else:
            print("Wrong arguments types for object Book")
            del self
            exit()

    def __check_name(self, name):
        return type(name) == str and len(name) > 0

    def get_recipe_by_name(self, name):
        for recipe in self.recipes_list:
            if recipe.name == name:
                return recipe
        return None

    def get_recipes_by_types(self, recipe_type):
        recipes = []
        for recipe in self.recipes_list:
            if recipe.recipe_type == recipe_type:
                recipes.append(recipe)
        return recipes

    def add_recipe(self, recipe):
        self.recipes_list.append(recipe)
        self.last_update = datetime.datetime.now()
