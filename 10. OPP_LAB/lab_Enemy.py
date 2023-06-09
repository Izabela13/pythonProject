"""
Polecenie:

1.
Chcemy, żeby Trolle zawsze miały 100 życia i 20 ataku HINT: super().
Chcemy mieć konstruktor, który nie przyjmuje parametrów zycia i ataku

2.
Dopisać kolejnego przeciwnika
Zawsze ma 200 życia, ale różna siła ataku

3.
Kolejny przeciwnik nie będzie mógł atakować jeżeli jego życie spadnie poniżej 20 puntków.
Przyjmuje 2 razy mniejsze obrażenia, jeżeli jego życie spadnie poniżej 50.
"""


class Enemy:

    def __init__(self, name='Enemy', health=0, hit_power=0):
        self.name = name
        self.health = health
        self.hit_power = hit_power

    def take_damage(self, damage):
        remaining_health = self.health - damage
        if remaining_health > 0:
            self.health = remaining_health
        else:
            self.health = 0
            print(f"{self.name} is dead.")

    def attack(self):
        print(f"Enemy attack with power {self.hit_power}")

    def __str__(self):
        return f"Name {self.name}. Health: {self.health}. Hit power: {self.hit_power}"


class Troll(Enemy):

    # 1. Definiowanie konstruktora "__init__".
    def __init__(self, name):  # Oczekiwanie, że podane zostanie nazwa Trolla.
        super().__init__(name, 100, 20)  # Przekazujemy nazwę, 100 życia, 20 do hit_power.
        # Pełna składania metody super(): super(Troll, self).__init__()

    def take_damage(self, damage):
        super().take_damage(damage)
        if self.health == 0:
            self.health = 100


# 2. Dopisanie innego przeciwnika, który ma 200 życia, ale różna siła ataku
class Buka(Enemy):  # Nasz kolejny przeciwnik dziedziczy po klasie "Enemy"

    def __init__(self, name, hit_power):  # Przesłaniamy konstruktor z nadklasy "Enemy".
        super().__init__(name=name, health=200, hit_power=hit_power)  # możemy podać nazwane parametry

    # 3.1. Buka nie będzie mógł atakować jeżeli jego życie spadnie poniżej 20 puntków
    def attack(self):  # przesłaniamy metode z nadklasy "Enemy"
        if self.health < 20:  # Jeżeli zdrowie jest poniżej 20 pkt, to
            return  # nic nie robi --> zabezpieczenie (technika defensywnego programowania)
        super(Buka, self).attack()

    # 3.2. Buka przyjmuje 2 razy mniejsze obrażenia, jeżeli jego życie spadnie poniżej 50.
    def take_damage(self, damage):  # przesłonięcie metody "take_damage" z nadklasy "Enemy"
        if self.health < 50:  # jeżeli zdrowie spadnie poniżej 50 pkt, to...
            super().take_damage(damage/2)  # biorze obrażenia przez pół mniejsze
        else:                              # w przeciwnym razie...
            super().take_damage(damage)    # damage jest taki, jaki wymierzony w Buke


troll = Troll("Troll")
"""
gdyby zostawić taki zapis: 
    troll = Troll("Troll", 100, 100)
to dwa ostatnie argumenty zostaną podświetlone na żółto jako te, których PyCharm się nie spodziewa.
Przesłoniliśmy nasz konstruktor. Mamy więc konstruktor, który nie przyjmuje parametrów życia i ataku. 
"""
print(troll)  # Name Troll. Health: 100. Hit power: 20
print()

# # Udowodnienie, że implementacja nowej klasy jest w porządku:
# buka = Buka("Buka", 50)  # 200 HP zawsze
# print(buka)  # Name Buka. Health: 200. Hit power: 50
# print(buka.attack())  # Enemy attack with power 50 --> OK, ma więcej niż 20 pkt zdrowia
# buka.take_damage(150)  # Name Buka. Health: 50. Hit power: 50
# print(buka)
"""
Wyniki: 
Name Buka. Health: 200. Hit power: 50
Enemy attack with power 50
None
Name Buka. Health: 50. Hit power: 50
"""


# # Czyścimy drania:
# buka = Buka("Buka", 50)  # 200 HP zawsze
# print(buka)
# print(buka.attack())
# buka.take_damage(151)
# print(buka)
# buka.take_damage(49)
# print(buka)
"""
Wyniki: 
Name Buka. Health: 200. Hit power: 50
Enemy attack with power 50
None
Name Buka. Health: 49. Hit power: 50
Name Buka. Health: 24.5. Hit power: 50
"""

buka = Buka("Buka", 50)  # 200 HP zawsze
print(buka)
print(buka.attack())
buka.take_damage(151)
print(buka)
buka.take_damage(49)
print(buka)
buka.take_damage(10)
print("Should attack")
buka.attack()
"""
Wyniki: 
Name Buka. Health: 200. Hit power: 50
Enemy attack with power 50
None
Name Buka. Health: 49. Hit power: 50
Name Buka. Health: 24.5. Hit power: 50
Should attack

Jak sobie to przeanalizujemy, to widzimy, że jeżeli spadliśmy ze zdrowiem poniżej 50 pkt, nasz "hit" jest dzielony na pół. 
Jeśli spadniemy poniżej 20 pkt zdrowia, nasz Buka nie atakuje dlatego, że jego zdrowie spadło poniżej 20 pkt (return). 
"""