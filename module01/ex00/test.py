from book import Book
from recipe import Recipe

if __name__ == "__main__":
    first_book = Book("test1")
    sandwich = Recipe("sandwich", 5, 10, ["ham", "cheese", "salad", "tomatoes"], "a good thing", "lunch")
    cake = Recipe("cake", 4, 15, ["egg", "flour", "sugar", "butter"], "yummy", "dessert")
    first_book.add_recipe(sandwich)
    first_book.add_recipe(cake)
    print(first_book.get_recipe_by_name("sandwich"))
    for recipe in first_book.get_recipes_by_types("dessert"):
        print(recipe)
