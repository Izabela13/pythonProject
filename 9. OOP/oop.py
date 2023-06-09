# Klasa główna "Animal"

class Animal(object):
    pass  # Klasa nic nie będzie robiła


"""
Klasa "Animal" pod spodem dziedziczy po innej klasie. Nie podaliśmy tego w kodzie dlatego, że jest to zachowanie domyślne
w Pythonie w wersji 3. Jeżeli chcielibyśmy, aby kod był kompatybilny z Pythonem w wersji 2, musielibyśmy dopisać w 
nawiasię nadklasę "objekt". Nadklasa "object" jest nadklasą dla wszystkich klas, które są towrzone w Pythonie: 

    class Animal(object): 
        pass

Jeśli zaznaczymy "object" i naciśniemy [ctrl + B], to zobaczymy, że klasa "object" ma dokumentację.   
Klasa "object" jest to klasa podstawowa dla całej hierarchii klas. 
Klasa "object" ma zdefiniowane metody. Jeśli klasy dziedziczą po nadklasie "object", to w klasach są już obecne metody.
Poszczególne metody nie mają implementacji. 
Jest to pierwsze pudełko na wszystkie nasze klasy. Od tej klasy zaczyna się dziedziczenie.
"""


class Dog(Animal):  # klasa "Dog" dziedziczy po klasie "Animal"
    pass


class Owczarek(Dog):  # rozwinięcie dziedziczenia - podklasa psa. Owczarek dziedziczy po "Dog".
    pass


class Cat(Animal):  # klasa "Cat" dziedziczy po klasie "Animal"
    pass


########################################################################################################################

"""
Badanie klas - FUNKCJA ISSUBCLASS
"""

"""
Funkcja ISSUBCLASS przyjmuje jako argumenty nasze klasy. Możemy sprawdzić, czy np. klasa "Cat" jest subklasą "Animal".
Żeby zobaczyć, co zwróci funkcja trzeba zastosować funkcję print()
"""

# print(issubclass(Cat, Animal))  # True --> "Cat" jest podklasą "Animal"
# print(issubclass(Dog, Animal))  # True --> "Dog" jest podklasą "Animal"

"""
W PyCharmie widać, że koło klasy "Animal" pojawiła się ikonka kółka ze strzałką w dół. Ta ikonka podpowiada nam, że 
po klasie "Animal" dziedziczą inne klasy. 
"""

# print(issubclass(Animal, Animal))  # True - klasa "Animal" NIE DZIEDZICZY PO SAMEJ SOBIE

"""
Klasa "Animal" nie dziedziczy po samej sobie, ale jest samą sobą. Wszystkie metody, które są dostępne w klasie "Animal", 
są również dostępne w klasie "Animal".
"""

# print(issubclass(Dog, Cat))  # False
# print(issubclass(Cat, Dog))  # False

"""
Kot nie jest psem, pies nie jest kotem. 
"""


# print(issubclass(Owczarek, Dog))     # True
# print(issubclass(Owczarek, Animal))  # True
# print(issubclass(Owczarek, object))  # True

"""
Owczarek to podklasa klasy "Dog". Owczarek dziedziczy po psie, pies dziedziczy po "Animal". 
Jest to przykład wielopoziomowego dziedziczenia (multilevel inheritance): A --> B --> C. 
Jeżeli "C" dziedziczy po "B", to również dziedziczy po "A". 

[Animal] --> [Dog] --> [Owczarek] - Owczarek jest subklasą Animala. 
Owczarek jest też podklasą dla klasy "object". 

Gdyby jednak odwrócić kolejność, np. 
    print(issublass(Dog, Owczarek)
Pojawi się "False", ponieważ "Dog" nie jest subklasą/ podklasą dla "Owczarka". Jest na odwrót. 
"""


########################################################################################################################

"""
Badanie klas - FUNKCJA ISINSTANCE
"""

dog = Dog()  # inicjacja pierwszego psiaka

# print(isinstance(dog, object)) # True --> "dog" jest instancją nadklasy "object".
# print(isinstance(dog, Animal)) # True --> "dog" jest instancją "Animal", bo dziedziczy po klasie "Animal"
# print(isinstance(dog, Dog))    # True --> dog dziedziczy po klasie "Dog"
# print(isinstance(dog, Cat))    # False -->

"""
W "isinstance" podajemy referencję, czyli obiekt, który jest już zainicjalizowany (istnieje w pamięci komputera). 
W pierwszym przykładzie sprawdzamy, czy "dog" jest instancją "Animal". 
W drugim przykładzie sprawdzamy, czy "dog" jest instancją klasy "Dog".
"""


########################################################################################################################

"""
Badanie klas - IS
"""

dog_1 = Dog()
dog_2 = dog  # "dog_2" to tak naprawdę "dog"
# # Tworzymy dokładnie dwa obiekty (dog_1 i dog_2)

print(dog is dog)    # True --> przekazujemy dwa razy instancję
print(dog is dog_1)  # False -->
print(dog is dog_2)  # True -->

"""
W wynikach chodzi o obiekty. Fizycznie tworzymy dwa obiekty: 
    dog = Dog()
    dog_1 = Dog()
    dog_2 = dog
Mamy referencje do tych obiektów. "dog" i "dog_2" wskazują na ten sam obiekt w pamięci, a "dog_1" wskazuje na inny. 
"""

# Do funkcji print() wrzucamy instancje
print(dog)
print(dog_1)
print(dog_2)
"""
Wynik: 
<__main__.Dog object at 0x000001CBC7782AD0>
<__main__.Dog object at 0x000001CBC7782B90>
<__main__.Dog object at 0x000001CBC7782AD0>

To, co się pojawiło jest związane z pamięcią i fizycznym miejscem w pamięci, w którym istnieje nasz obiekt. 
Jeśli się przyjrzeć uważnie, to pierwszy i trzeci wynik, czyli "dog" i "dog_2" mają dokładnie te same miejsca w pamięci. 
Utworzyliśmy dwa obiekty i trzy różne referencje. 

Domyślne zachowanie funkcji print() - jeżeli przekażemy do funkcji print() obiekt, który nie ma zaimplementowanej/ nadpisanej
metody str (przedstawiania obiektu w postaci stringowej), to funkcja print() wydrukuje miejsce tego obiektu w pamięci.
"""

print(__name__)
"""
Wynik: 
--main__

__name__ to __main__ --> PRZEJDŹ DO PLIKU "oop_2.py"
"""