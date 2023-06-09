from abc import ABC, abstractmethod
import mock_database
import sys


class Strategy(ABC):  # Klasa ogólna z jakąś metodą, którą będą musiały zaimplementować wszystkie różne strategie
    """
    Metoda abstrakcyjna - nic nie robi.
    """
    @abstractmethod
    def execute(self):  # to będą różne rzeczy
        pass


class ListIngredients(Strategy):  # ta klasa dziedziczy po klasie "Strategy"
    def execute(self):  # dodawanie logiki do metody 'execute'
        all_ingredients = mock_database.find_all()  # importowanie metody 'find_all()' z 'mock_database'
        for i in all_ingredients:
            print(i)


class ListIngredientsByNameLike(Strategy): # dziedziczenie po klasie "Strategy"
    def execute(self):  # rozszerzenie metody 'execute' --> wylistuj mi składniki po nazwie zawierającej ciąg znaków
        ingredient_name = input("Proszę podać nazwę składnika: ")  # to trafi do metody "find_by_name_like"
        result = mock_database.find_by_name_like(ingredient_name)  # z 'mock_database' implementacja metody 'find...'
        for i in result:
            print(i)


class AddNewIngredient(Strategy):  # Nowa strategia
    def execute(self):  # przysłonięcie metody 'execute' z nadklasy
        print("Dodawanie nowego składnika")
        name = input("name: ")
        calories = input("calories: ")
        protein = input("protein: ")
        fat = input("fat: ")
        carbs = input("carbs: ")
        fiber = input("fiber: ")
        ingredient_type = input("ingredient Type: ")
        mock_database.add_ingredient(name, calories, protein, fat, carbs, fiber, ingredient_type)


class TerminateProgram(Strategy):  # Ostatnia strategia - terminowanie działania programu
    def execute(self):
        sys.exit()  # kończy działanie programu - korzystamy z modułu sys.