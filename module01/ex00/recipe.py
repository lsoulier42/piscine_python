class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if self.__check_name(name) \
            and self.__check_cooking_lvl(cooking_lvl) \
            and self.__check_cooking_time(cooking_time) \
            and self.__check_ingredients(ingredients) \
            and self.__check_description(description) \
            and self.__check_recipe_type(recipe_type):
            self.name = name
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.description = description
            self.recipe_type = recipe_type
        else:
            print("Wrong arguments types for object Recipe")
            del self
            exit()

    def __str__(self):
        txt = ""
        txt += "Name: " + self.name + "\n"
        txt += "Cooking level: " + str(self.cooking_lvl) + "\n"
        txt += "Cooking time: " + str(self.cooking_time) + " minutes\n"
        txt += "Ingredients: "
        nb_ingredients = len(self.ingredients)
        for i in self.ingredients:
            txt += i
            if i == self.ingredients[nb_ingredients - 1]:
                txt += '\n'
            else:
                txt += ', '
        if self.description:
            txt += "Description: " + self.description + "\n"
        txt += "Recipe type: " + self.recipe_type + "\n"
        return txt

    def __check_name(self, name):
        return type(name) == str and name

    def __check_cooking_lvl(self, cooking_lvl):
        return type(cooking_lvl) == int and cooking_lvl in range(1, 6)

    def __check_cooking_time(self, cooking_time):
        return type(cooking_time) == int and cooking_time > 0

    def __check_ingredients(self, ingredients):
        if type(ingredients) == list and len(ingredients) > 0:
            for i in ingredients:
                if type(i) != str:
                    return False
            return True
        else:
            return False

    def __check_description(self, description):
        return type(description) == str

    def __check_recipe_type(self, recipe_type):
        return type(recipe_type) == str and recipe_type in ["starter", "lunch", "dessert"]