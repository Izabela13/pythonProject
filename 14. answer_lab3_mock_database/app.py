import loader
from prgoram_strategy import AddNewIngredient, ListIngredients, ListIngredientsByNameLike, TerminateProgram


if __name__ == '__main__':  # Jeżeli nazwa programu to "main", uruchamiaj całą logikę programu
    loader.load_initial_data()  # Na starcie programu, załaduj wszystkie składniki
    strategy_map = {
        "1": AddNewIngredient(),  # instancja klasy "AddNewIngredient"
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
            strategy_map[decision].execute() # z mapy strategii wywołujemy 'execute'.
            print("\n")