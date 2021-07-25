def set_recipe(prep_time, meal_type, ingredients):
    return {
            'ingredients': ingredients,
            'meal': meal_type,
            'prep_time': prep_time
        }


def print_keys():
    print(*cookbook)


def print_values():
    print(*cookbook.values())


def print_items():
    print(cookbook)


def print_recipe(recipe_name):
    recipe = cookbook[recipe_name]
    print("Recipe for {}:".format(recipe_name))
    print("Ingredients list: {}\nTo be eaten for {}.\nTakes {} minutes of cooking.\n".format(recipe['ingredients'], recipe['meal'], recipe['prep_time']))


def delete_recipe(recipe_name):
   cookbook.pop(recipe_name)


def add_recipe(recipe_name, meal_type, prep_time, ingredients):
    cookbook[recipe_name] = set_recipe(prep_time, meal_type, ingredients)


def promp_get_recipe():
    print("Please enter the recipe's name to get its details: ")
    recipe_name = input()
    if recipe_name in cookbook:
        print_recipe(recipe_name)
    else:
        print("Recipe not found\n")


def prompt_delete_recipe():
    print("Please enter the recipe's name to delete: ")
    recipe_name = input()
    if recipe_name in cookbook:
        delete_recipe(recipe_name)
    else:
        print("Recipe not found\n")
    print("You have successfully deleted the recipe {} from your cookbook.\n".format(recipe_name))


def prompt_new_recipe():
    print("Enter the new recipe name:")
    recipe_name = input()
    print("Enter the ingredients (press enter w/o ingredient to stop listing):")
    ingredients = []
    new_ingredient = 'bidule'
    while new_ingredient:
        new_ingredient = input()
        if new_ingredient:
            ingredients.append(new_ingredient)
    print("Enter the type of meal: ")
    meal_type = input()
    print("Enter the preparation time: ")
    prep_time = 'a'
    while not prep_time.isdigit():
        prep_time = input()
        if not prep_time.isdigit():
            print("Please enter an integer value")
    add_recipe(recipe_name, meal_type, int(prep_time), ingredients)
    print("You have successfully added the recipe {} to your cookbook\n".format(recipe_name))


def prompt():
    selection = '0'
    choices = ['1', '2', '3', '4', '5']
    fctArray = [prompt_new_recipe, prompt_delete_recipe, promp_get_recipe, print_items]
    while selection != '5':
        print(
            "Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n>>",
            end='')
        choice = input()
        if choice not in choices:
            print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")
        elif choice == '5':
            print("Cookbook closed.")
            break
        else:
            fctArray[int(choice) - 1]()


if __name__ == "__main__":
    cookbook = {
        'sandwich': set_recipe(10, 'lunch', ['ham', 'bread', 'cheese', 'tomatoes']),
        'cake': set_recipe(60, 'dessert', ['flour', 'sugar', 'eggs']),
        'salad': set_recipe(15, 'lunch', ['avocado', 'arugula', 'tomatoes', 'spinach'])
    }
    prompt()
