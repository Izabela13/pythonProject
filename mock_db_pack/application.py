""" Application for mock database """


import loading_system
from program_strategy import AddNewIngredient, ListIngredients, ListIngredientsByNameLike, TerminateProgram


if __name__ == '__main__':
    loading_system.load_initial_data()  # Data loading
    strategy_map = {
        "1": AddNewIngredient(),
        "2": ListIngredients(),
        "3": ListIngredientsByNameLike(),
        "0": TerminateProgram()
    }

    while True:
        print("1 - Dodaj składnik",
            "2 - Pokaż wszystkie",
            "3 - Szukaj po nazwie",
            "0 - Zakończ",
            "Wybierz, co, chcesz zrobić: ", sep='\n')
        decision = input("> ")

        if decision not in strategy_map:
            print("Proszę wybrać poprawną wartość")
        else:
            strategy_map[decision].execute()
            print("\n")