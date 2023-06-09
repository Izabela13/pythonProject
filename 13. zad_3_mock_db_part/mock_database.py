""" UDAWANA BAZA DANYCH """
"""
Napisz program konsolowy który:
1.	Podczas uruchomienia wczyta dane z pliku ingredients.csv i zachowa je w wybranej przez siebie strukturze danych 
2.	Po uruchomieniu w konsoli wyświetli menu z 4 możliwościami
1 – Dodanie nowego składnika
2 – Wyświetlenie wszystkich składników
3 – Wyświetlenie składnika po nazwie (like)
0 – Zakończenie programu
"""

from ingredient import Ingredient

ingredients = []  # tworzenie listy składników


def add_ingredient(name, calories, protein, fat, carbs, fiber, ingredient_type) -> None:  # metoda nie zwraca nic
    ingredients.append(Ingredient(name, calories, protein, fat, carbs, fiber, ingredient_type))


def find_all():  # W tej metodzie chcemy zwrócić nasze "ingredients"
    """
    Find all ingredients in list.
    :return: List of ingredients
    """
    return ingredients.copy()  # zwrócimy kopię tablicy (listy) "ingredients", ale nie samą tablicę


def find_by_name_like(name: str):
    """
    Find all ingredients by name like
    :param name: name 'like'
    :return: list of ingridients
    """
    copy = find_all()
    result = []

    for ingredient in copy:
        if name.casefold() in ingredient.name.casefold(): # Jeżeli nazwa składnika zawiera część, którą podamy ...
            result.append(ingredient) # ... dodamy składnik do listy "result"