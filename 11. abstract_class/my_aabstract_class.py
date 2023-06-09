""" METODA ABSTRAKCYJNA """
"""
Metoda abstrakcyjna to taka metoda, która w naszej nadklasie jest zdefiniowana, ale nie posiada implementacji. 
Czasem jest tak, że nie wiadomo, jak ma się zachowywać dana metoda, ale wiadomo, że podklasy muszą mieć dany 
rodzaj metody. 

Np. klasa Animal i metoda "move". 
Nie bardzo wiadomo, co zaimplementować w klasie "Animal". Nie jest to jeszcze żadne zwierzę, a ogólna klasa "Animal". 
Nie ma jakichś szczególnych cech poruszania się. Nie bardzo wiadomo, co można by zaimplementować. W tym momencie można
stworzyć METODĘ ABSTRAKCYJNĄ "move". 
Jeśli storzymy jakieś podklasy dla klasy "Animal" (Dog, Cat, etc.), to sam PyCharm podpowie, że mamy metodę abstrakcyjną
do dyspozycji i możemy zaimplementować jakieś jej działanie. 

Jest to taki rodzaj programowania, w którym chcemy mieć pewność, że ktoś dany rodzaj metody zaimplementuje. 
Np. Chcemy żeby pies biegał, żeby ptak latał, żeby wąż pełzał. Nie można tego pominąć. 
"""

"""
Każda nasza klasa dziedziczy po takiej "GodClass", która nazywa sie "object". 
Jeśli chcemy zaimplementować jakąś abstrakcję, przychodzi nam z pomocą z pakietu "abc" (tak został nazwany) klasa ABC.
Nasza klasa musi rozszerzać klasę "ABC". 

METODA ABSTRAKCYJNA TO TAKA, KTÓRA NIE MA CIAŁA (NIE MA LOGIKI), ALE SŁUŻY DO TEGO, ABY PODKLASY IMPLEMENTOWAŁY 
PEWNĄ LOGIKĘ. 
"""

from abc import ABC, abstractmethod


class AbstractClass(ABC):

    def __init__(self, value):  # Tworzymy konstruktor
        self.value = value
        super().__init__()  # Teraz wywołujemy metodę "__init__" z nadklasy, czyli w tym wypadku z klasy "ABC".

    @abstractmethod  # DEKORATOR (zostanie wyjaśniony w przyszłości)
    def foo(self):  # definiujemy metodę "foo"
        pass        # z założenia metoda abstrakcyjna nie ma żadnej implementacji

    def test(self):  # mogą być też inne metody, pozaabstrakcyjne.
        print("Test")


class MyClass(AbstractClass):  # Tworzymy klasę, która będzie dziedziczyła po klasie "AbstractClass".

    def foo(self):  # nadpisanie metody "foo" z nadklasy.
        print(f"Implemented! Value is {self.value}")


my_class = MyClass(11)
my_class.foo()
print("WORKS")

"""
Jeżeli dodamy nową klasę, która będzie dziedziczyła po klasie "AbstractClass" (mającej metodę abstrakcyjną), np.:
    
    class MyClass(AbstractClass):
        pass
        
PyCharm podkreśli wężykiem nazwę klasy i przekaże informację "Klasa MyClass musi zaimplementować wszystkie abstrakcyjne
metody (Class MyClass must implement all abstract methods), nie zaimplementowałeś wszystkich abstrakcyjnych metod, a jest
to istotne dla działania programu". 

Zamysł jest taki, że wszystkie klasy, które dziedziczą po nadklasie posiadającej jakąś metodę abstrakcyjną, będą tę
metodę abstrakcyjną nadpisywać (dołożą "coś" do niej).  

Nie oznacza to, że jeśli puścimy program, pojawi się wyjątek. 
W Pythonie jest to trochę jak z dostępem do metod prywatnych.
Działa to na zasadzie podpowiedzi - "zaimplementuj metodę abstrakcyjną, bo taki był zamysł autora". 

zaznaczenie klasy + [ctrl + o] --> pojawi się drzewko dziedziczenia 
Widać w tym drzewku, że w klasie "AbstractClass" mamy dwie metody do nadpisania - "__init__" albo "foo".

Klasa może mieć dowolną ilość metod abstrakcyjnych i nieabstrakcyjnych. 
"""