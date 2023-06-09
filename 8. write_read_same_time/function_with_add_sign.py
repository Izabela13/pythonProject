""" WYJAŚNIENIE ZNAKU -> W FUNKCJI """


def sorted_key(d: dict) -> str:  # typowanie argumentu
    return d['athlete']          # co zostanie zwrócone z funkcji


"""
W funkcji nadajemy jakiś argument. W tym przykładzie nazywany został 'd'. 

Składnia (d: dict). 
W przypadku słowników nie można przeprowadzić sortowania wprost, korzystając z metody sorted(). 
Typujemy. Chcemy przekazać, że dla zmiennej 'd' oczekujemy słownika 'dict'. 

IneliJ podpowie od razu przy wpisaniu zmiennej, czy jest ona poprawna. Np. 
    sort_key("Andrzej") 
Od razu pojawi się podpowiedź, że program oczekuje słownika, a przekazany został string. 
Zanim zostanie wywołany program, wiemy, że coś jest nie tak. Używamy funkcji nie w ten sposób, jak powinniśmy. 

Przy próbie wprowadzenia stringa program również podpowie, że jest tu niespójność. Nie zrobimy operacji na stringu.

    def sort_key(d: str) -> str:
        return d['athlete']
        
    sort_key("Andrzej")
    sort_key({})
    
Podsumowując: 
1. Zapis 

    def sorted_key(d: dict) -> str:

jest podpowiedzią, co użytkownik powinien przekazać JAKO ARGUMENT DO METODY.

2. Symbol -> to podpowiedź dla kogoś, kto korzysta z funkcji. 
Jeśli nacisniemy [ctrl + q] wyświetli się mała dokumentacja, co dana funkcja robi. 
Po najechaniu na "sort_key" dana osoba widzi podpowiedź, że funkcja zwróci stringa. 
W innym przypadku funkcja może zwracać inty, itd. 
Ta strzałka -> to ułatwienie (żeby ktoś, kto korzysta z funkcji wiedział, czego się spodziewać). 
"""


def sort_key(d: dict) -> str:
    """
    :param d:
    :return:
    """
    return d['athlete']


"""
Dokumentacja metody
"""

"""
Parametrem 'd' dla funkcji będzie jej dana wejściowa. Sortowanie tabeli ze słownikami. W funkcji jest podane, że 
'sort_key' przyjmuje słownik. Czyli dla tej funkcji parameterm wejściowym będzie cały wiersz: 
    {'athlete': 'CASLAVSKA, Vera', 'gold': 7, 'silver': 4, 'bronze': 0, 'country': 'Czechoslovakia', 'total': None},
"""


def print_name():
    print("Andrzej")


zmienna_name = print_name

"""
To, co możemy zrobić z funkcją 'print_name()', to zrobić zmienną ('zmienna_name'), do której możemy przypisać funkcję
'print_name' (bez nawiasów). Zmienną przypisaliśmy do metody. 
"""

zmienna_name()

"""
Zmienną "zmienna_name" możemy wywołać tak, jakby była metodą --> zmienna_name(). 
Ta zmienna powinna wyprintować na konsolę wartość "Andrzej". 

Tak samo jest w przykładzie. Przekazujemy do parametru 'key' naszą metodę 'sort_key', ale bez nawiasów.
Nasza metoda 'sort_key' jest przypisana teraz do zmiennej 'key'. 

Wewnątrz jest implementacja, która przekazuje do programu informację "POSORTUJ MI PO 'key()'. 

"Jestem przypisany do funkcji 'sort_key()'. Wywołuję funkcję. Mam parametr wejściowy '(d: dict)'. Sortuję po kolejnym 
obiekcie w tej mapie. Porównuję kolejne słowniki. Włożyłem obiekt do funkcji. Na każdej mapie będę zwracał wartość
    'athlete': 'XXXXX, Yyyy' 
Teraz nie porównuję map, porównuję stringi".

Prawdopodobnie jeśli wywołamy key() i nie podamy parametru, prawdopodobnie otrzymamy wartość, która wejdzie do funkcji.
"""