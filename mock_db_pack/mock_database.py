""" Mock database elements """


from Ingredient_class import Ingredient

ingredients = []  # The list for all ingredients


def add_ingredient(name, calories, protein, fat, carbs, fiber, ingredient_type) -> None:
    """
    Add new ingredient to 'ingredients' list.
    :param name:
    :param calories:
    :param protein:
    :param fat:
    :param carbs:
    :param fiber:
    :param ingredient_type:
    :return:
    """
    ingredients.append(Ingredient(name, calories, protein, fat, carbs, fiber, ingredient_type))


def find_all():
    """
    Find all ingredients in list and return a copy.
    :return: List of Ingredients
    """
    return ingredients.copy()


def find_by_name_like(name: str):
    """
    Find all ingredients by name like
    :param name: name 'like'
    :return: list of ingredients
    """

    copy = find_all()
    result = []

    for ingredient in copy:
        if name.casefold() in ingredient.name.casefold():
            result.append(ingredient)
    return result
