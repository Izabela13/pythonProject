""" POLIMORFIZM """

"""
Polimorfizm w Pythonie jest tak naturalny, że my go nawet nie widzimy.
W poniższych przykładach działą polimorfizm. 
"""

a = 1
b = 'string'
c = 1, 2, 3
d = {'key': 1}

print(a)
print(b)
print(c)
print(d)

"""
Wynik: 
1
string
(1, 2, 3)
{'key': 1}
"""

"""
Polimorfizm jest traktowaniem obiektów w jakiś jednakowy sposób.
To, co zrobiliśmy w powyższych przykładach można określić jako potraktowanie obiektów w jakiś jednakowy sposób. 
W jaki? Printujemy te obiekty na konsolę. 

Funkcja print() przyjmuje jakieś argumenty. W tym przykładzie przyjmuje:
- jakiegoś 'inta', 
- jakiegoś 'stringa', 
- jakiegoś 'tupla', 
- jakieś dictionary.

Wszystkie te obiekty posiadają metodę odpowiedzialną za przekształcenie tego obiektu na reprezentację tekstową. 
Innymi słowy posiadają reprezentację jako "string", który widzimy na konsoli. 

Już na tych przykładach działa polimorfizm - traktujemy wszystkie obiekty różnych typów w ten sam sposób - print(). 

W Pythonie polimorfizm można osiągnąć nie stosując dziedziczenia.
"""
print()


"""
Polimorfizm na przykładzie dziedziczenia w klasach. Każda klasa będzie miała metodę "introduce". 
"""


class A:
    def introduce(self):
        print("I'm A")


class B:
    def introduce(self):
        print("I'm B")


class C:
    def different(self):
        print("Different")


my_list = [A(), B()]  # dodanie klasy C spowoduje błąd, ponieważ nie ma metody "introduce".

for poli_class in my_list:
    poli_class.introduce()

"""
Traktujemy klasę A i B jednakowo i otrzymujemy wynik: 
I'm A
I'm B

Byłoby to niemożliwe w innych językach programowania. W innych językach silnie stypowalibyśmy naszą listę. 
Np. byłaby to lista, która przyjmuje tylko klasę "A" albo tylko klasę "B". Do listy, która przyjmuje np. tylko klasę "A"
nie moglibyśmy wstawić jakiejś klasy "B". W takich językach programowania trzebabyłoby wprowadzić jakąś nadklasę i obie
klasy ("A" i "B") musiałyby rozszerzać nadklasę. I dopiero wtedy obie klasy traktowane byłyby w ten sam sposób. 

Jeśli dopiszemy klasę "C", nie będziemy mogli dodać jej do naszej listy dlatego, że klasa "C" nie ma metody "introduce". 
W tym wypadku mamy złamanie tego polimorfizmu. 

Jest takie stwierdzenie, że jeśli "coś chodzi wygląda jak kaczka, chodzi jak kaczka i kwacze jak kaczka, to musi być kaczką. 
(duck typing)

Nasz polimorfizm uzyskujemy nie przez typy obiektów, nie przez wspólną klasę, ale agregujemy je w ten polimorfizm 
poprzez dostarczenia odpowiednich metod. 

Jeżeli chcielibyśmy naprawić działanie naszego programu, to wystarczyłoby, żebyśmy do klasy "C" dopisali również 
metodę "introduce()". W tym momencie wszystko będzie się zgadzać, tj. "chodzi jak kaczka, kwacze jak kaczka, musi być
kaczką". Tutaj - potrafi się przedstawić, polimorfizm mamy załatwiony. 

Dlatego w Pythonie polimorfizm jest przezroczysty (przez to, że jest tu "duck typing"), czyli że definiujemy polimorfizm
przez nasze metody. 

Moglibyśmy naprawić program, np. klasa "C" dziedziczyłaby po klasie "B". 
Uwaga, jeśli "C" ma dziedziczyć po obu klasach, metoda introduce będzie zależała od KOLEJNOŚCI, w jakiej podamy klasy.
"""