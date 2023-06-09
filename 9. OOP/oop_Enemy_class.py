""" TWORZENIE GRY """

"""
Mamy storzyć grę, w której będą jacyś przeciwnicy (enemys). 
"""


class Enemy:  # klasa Enemy dziedziczy po klasie "object"

    """ Dodawanie metod """

    """ 
    Metoda __init__ 
    Nasz przeciwnik musi mieć jakąś nazwę (domyślnie "Enemy"), musi mieć jakieś zdrowie ("health") i musi nas bić
    (hit_power). Inicjujemy poszczególne zmienne. Każdy przeciwnik będzie w ten sam sposób inicjalizowany. 
    """
    def __init__(self, name='Enemy', health=0, hit_power=0):
        self.name = name
        self.healht = health
        self.hit_power = hit_power

    """ 
    Metoda zadająca obrażenia - żebyśmy mogli bić przeciwnika. 
    Implementacja logiki funkcji - jeśli zdrowie spadnie do zera lub poniżej, to przeciwnik umiera. 
    """
    def take_damage(self, damage):  # oczekujemy jakichś obrażeń
        remaining_healht = self.healht - damage  # jeżeli enemy przyjumuje jakiś damage, to jeśli...
        if remaining_healht > 0:  # ... pozostałe zdrowie jest większe od zera, to nie utłuklismy naszego przeciwnika...
            self.healht = remaining_healht  # ... i jego zdrowie jest równe temu, co zostało, ...
        else:                # ... w innym wypadku znaczy, że go zabiliśmy.
            self.healht = 0  # Ustawiamy zdrowie na 0, żeby nie schodzić poniżej 0 dla zdrowia.
            # print("Enemy is dead.")  """ Rozwijamy ten fragment """
            print(f"{self.name} is dead.")  # Przekazując nazwę wroga będzie wiadomo, który rodzaj wroga dednął.

    def attack(self, additional_attack: int):
        print(f"Enemy attack with power {self.hit_power + additional_attack}")

    """
    Metoda __str__
    Metoda jest reprezentacją stringową dla obiektu. Z tej metody chcemy zwrócić wszystkie dane.
    Zaczynamy od "f", które służy formatowaniu
    """
    def __str__(self):
        return f"Name {self.name}. Health: {self.healht}, Hit Power: {self.healht}"  # wszystkie dane


"""
W naszym programie będą jacyś przeciwnicy, który będą dziedziczyć po klasie "Enemy". Będzie to klasa "Troll".

Przy metodzie "__str__" pojawiła nam się ikona, która wskazuje, że mamy nadpisaną metodę.
Metoda "__str__" z obiektu "Enemy" nadpisuje metodę z obiektu "object" (czyli z naszej Gotklasy).
Jeśli klikniemy w tę ikonkę, to program przekieruje nas do metody "__str__" w nadklasie "object". 

Przy klasie "Enemy" znowu widać ikonkę, która wskazuje, że po tym obiekcie dziedziczy jakaś klasa, w tym przykładzie 
nasz "Troll". 
"""


class Troll(Enemy):
    pass  # Na razie nic nie implementujemy.


########################################################################################################################

""" TWORZENIE INSTANCJI DLA KLASY, KTÓRA POSIADA NADKLASĘ """
"""
Nie dodając nic w klasie "Troll" możemy utworzyć sobie kilka jego INSTANCJI. 
"""

# # Tworzenie kilku instancji Trolla (złego przeciwnika)
# troll = Troll()
# troll_with_name = Troll("Troll")
# troll_with_health = Troll("Troll", 100)
# troll_with_hit_power = Troll("Troll", 100, 100) # dodajemy kolejne parametry dla metod

# print(troll)
# print(troll_with_name)
# print(troll_with_health)
# print(troll_with_hit_power)

"""
Nie zaimplementowaliśmy nic w naszej klasie. Wywołujemy jednak konstruktor z różnymi parametrami. 
Wiadmo, że takie wywołanie zadziała, ponieważ dziedziczymy po nadklasie, czyli dziedziczymy po naszym "Enemy". 
Nie musimy pisać konstruktora w naszej podklasie (czyli klasie "Troll"). Mamy dostęp do metod nadklasy "Enemy".
Nie trzeba implementować metod nadklasy, ponieważ zawsze są one dziedziczone po nadklasie. 
"""

"""
Wynik: 
Name Enemy. Health: 0, Hit Power: 0
Name Troll. Health: 0, Hit Power: 0
Name Troll. Health: 100, Hit Power: 100
Name Troll. Health: 100, Hit Power: 100

Dzięki wykorzystaniu metody __str__ możemy odczytać na konsoli dane tak, jak je zapisaliśmy w programie. 
Bez metody __str__ zamiast wyniku, który prezentuje się powyżej, dostalibyśmy ciąg znaków stanowiących miejsce, gdzie 
te dane przechowywane są w pamięci. 
"""

########################################################################################################################


""" UŻYWANIE METOD NADKLASY W KLASIE """
"""
Dziedziczymy po klasie "Enemy". W klasie "Enemy" mamy zdefiniowaną taką metode, jak "take_damage". 
Czy na naszej instancji "Troll" możemy użyć metody "take_damage"? Jak najbardziej. 
"""

# troll = Troll("Troll", 100, 100)

# troll.take_damage(50)
# print(troll)
# troll.take_damage(51)  # W tym momencie ubijemy naszego "Trolla"
"""
Wynik: 
Name Troll. Health: 50, Hit Power: 50
Enemy is dead.
"""

########################################################################################################################


""" ROZWIJANIE METOD """
"""
Rozwijamy teraz rozwijać metodę "take_damage". print("Enemy is dead") niewiele mówi. 

Wynik: 
Name Troll. Health: 50, Hit Power: 50
Troll is dead.

Teraz wiadomo, że chodzi o zabicie Trolla. Gdyby byli inni wrogowie, ma to znaczenie. 
"""

########################################################################################################################


""" JAK DOSTAĆ SIĘ DO METOD NADKLASY Z NASZEJ PODKLASY """
"""
Na naszej instancji "Troll" od razu możemy zastosować metodę "take_damage" i ona zadziała, mimo że jest zaimplementowana
w klasie "Enemy" (nadklasie w stosunku do klasy "Troll"). 

Teraz chcemy dostać się z naszej klasy "Troll" do metod w naszej klasie "Enemy". 
"""


# # Dopisujemy metody do "Trolla" (kod powinien znajdować się wyżej, ale to tylko ćwiczenia)
# class Troll(Enemy):
#     # Zaczynamy od metody o innej nazwie
#     def take_damage_troll(self, damage):  # Nowa zasada - jak zabijemy Trolla, Troll wstaje i ma drugie życie
#         self.take_damage(damage)  # Dostajemy się do metody z nadklasy "Enemy"
#         if self.healht == 0:  # Jak Trollowi zjedzie zdrowie do zera, ma powstać jeszcze raz
#             self.healht = 100  # Troll dostaje drugie zdrowie


# troll = Troll("Troll", 100, 100)

# troll.take_damage_troll(50)
# print(troll)
# troll.take_damage_troll(51)
# print(troll)
"""
Wynik: 
Name Troll. Health: 50, Hit Power: 50
Troll is dead.
Name Troll. Health: 100, Hit Power: 100

Wszystko się zgadza - Troll dostał 50 damage'u, potem 51 damage, zginął i znów powstał.
"""



""" ZMIANA SYGNATURY METODY - NAZYWANIE METODY W TEN SAM SPOSÓB """


class Troll(Enemy):
    def take_damage(self, damage):  # przesłonięcie metody z nadklasy (nasza klasa Troll zasłania "Enemy")
        super().take_damage(damage)
        if self.healht == 0:
            self.healht = 100 # Troll dostaje drugie zdrowie

    def attack(self):
        print(f"Troll attack with power {self.hit_power}")


"""
Jeśli nazwiemy metodę z podklasy w ten sam sposób, jak nazwana jest ona w nadklasie, to przesłaniamy ją.
Nasza klasa "Troll" przesłania nam metodę "take_damage" z klasy "Enemy". 
"""

troll = Troll("Troll", 100, 100)

troll.take_damage(50)
print(troll)
troll.take_damage(51)
print(troll)
"""
Jeśli będziemy chcieli dostać się ddo nadklasy przez "self.take_damage(damage)", dostaniemy błąd: 
    RecursionError: maximum recursion depth exceeded

Przez to, że odwoływaliśmy się do naszej funkcji przez "self" program zapętlił się. Chodzi o ten fragment kodu: 

    def take_damage(self, damage):   1
        self.take_damage(damage)     2
        ...

Program sprawdza, gdzie ma "self.take_damage" (linia 2). Jest w ona w linii wyżej. Potem schodzi znowu piętro niżej. 
Krąży tak w kółko między dwoma linijkami, aż w końcu program Python stwierdza, że już wystarczy, za daleko weszliśmy 
w funkcje rekursywne i terminuje program (do nikąd to nie prowadzi). 

W przypadku, gdzy przesłaniamy sobie nazwy metod czy same metody, z pomocą przychodzi słowo kluczowe SUPER. 
Jeżeli używamy metody "super()" żeby dostać się do funkcji, interpreter Pythona będzie wiedział, że ma wejść w metodę 
"take_damage" w klasie "Troll".

Bez metody "super()" sytuacja wygląda tak: 
Na początku tworzymy klasę "Troll", która dziedziczy po nadklasie "Enemy" i wywołujemy na niej funkcję "take_damage". 
Interpreter na początku patrzy, czy w klasie "Troll" jest metoda "take_damage". W tym momencie mamy taką metodę. 
Interpreter użyje metody "take_damage" z klasy "Troll". 
Jeżeli zaczęlibyśmy rozszerzać metode o dodakowe parametry, wówczas PyCharm sam podpowie, aby uzupełnić argumenty.

Interpreter Pythona sprawdza, że nadpisaliśmy metodę o tej samej nazwie. Wchodzi w klase "Troll" i nie przechodzi już
do klasy "Enemy" (nie widzi metody "take_damage" w klasie "Enemy"). 

Podumowanie: 
1. Przesłoniliśmy metodę "take_damage" z klasy "Enemy" w klasie "Troll". 
2. Wywołaliśmy metodę "take_damage" z nadklasy poprzez metodę "super()".
3. Użyliśmy implementacji metody i rozwinęliśmy metodę "take_damage" o nową logikę. 

W naszej klasie "Enemy" możemy odwołać się do metody "take_damage" przez słowo kluczowe "self". 

Przesłanianie to bardzo dobra technika programistyczna. Przez to wprowadzamy jakąś logikę konkretnie pod kątem 
danej klasy. 
"""


class OtherEnemy:
    pass


"""
Jeżeli dodamy nową klasę, np. "OtherEnemy", to w tym przykładzie ta klasa nie będzie miała funkcjonalności takiej jak 
klasa "Troll". W klasie "Troll" metoda "take_damage" ma dodatkową logikę, która nie będzie się ujawniać w innych klasach.

To jest też dobry przykład zamazanego polimorfizmu w Pythonie. 
"""

# # Tworzymy listę wszystkich klas
# list = [Enemy(), Troll(), OtherEnemy()]
"""
W liście przekazujemy naszych przeciwników i tak to działa, że iterujemy po liście i każdemu wrogowi wywołujemy metodę
"take_damage". 
"""

# for e in list:
#     e.take_damage(100)

"""
Gdybyśmy nie przysłonili metody "take_damage" w klasie "Troll", nastąpiłaby w "Trollu" defaultowa implementacja tej 
metody z klasy "Enemy". Gdybyśmy zmienili nazwę metody w klasie "Troll" z "take_damage" na np. "take_damage_troll", 
wówczas przy wywołaniu metody z nadklasy nasz "Troll" nie wstawałby ponownie. 

Wywołujemy dla wszystkich trzech klas metodę "take_damage" (polimorfizm rozmyty) i wierzymy, że implementacja każdej 
z tych klas zapewni logikę, o która nam chodzi. 
"""

# troll = Troll("Troll", 100, 100)
# troll.attack()
# troll.take_damage(50)
# print(troll)
# troll.take_damage(51)
# print(troll)

########################################################################################################################


""" DODANIE METODY DO NADKLASY I PODKLASY """
"""
Dodajemy metodę "attack" do klasy "Enemy" i do subklasy "Troll". Wpierwszym etapie jest to metoda bez argumentów. 
Jeżeli wywołamy metodę "ATTACK" na naszym Trollu, to w pierwszej kolejności metoda ta będzie szukana w klasie "Troll". 
Gybyśmy usunęli metodę "attack()" z klasy "Troll", wówczas program będzie szukał metody piętro wyżej - w klasie "Enemy".
Jeśli zmodyfikujemy metode w nadklasie, wówczas PyCharm podpowie nam, że w klasie "Troll" nie pasuje sygnatura, bo 
metoda "attack" przyjmuje jakiś argument. W definiowaniu metody w klasie "Troll" fragment kodu, gdzie znajduje się słowo
kluczowe "self" podświetli się na żółto. PyCharm sugeruje, że może być to błąd. Nie oznacza to, że jest to faktyczny błąd.
Metoda "attack" wywoła się na "Trollu". Gdybyśmy chcieli wprowadzić dodatkowy argument, PyCharm podświetli fragment kodu
jako formę informacji, że nie jest to nadklasa i nie powinno być w tym miejscu dodatkowego argumentu. 
"""