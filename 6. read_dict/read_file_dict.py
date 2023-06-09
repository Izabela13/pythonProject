import csv

filename = 'username.csv'

"""
Nie musimy przekazywać parametru 'r', ponieważ jest on parametrem domyślnym. 
"""

with open(filename, encoding='utf-8', newline='') as user_file:
    reader = csv.reader(user_file, delimiter=';')

    for row in reader:
        print(row)
"""
Wynik:
['Username', 'Identifier', 'First name', 'Last name', 'Age']
['booker12', '9012', 'Rachel', 'Booker', '44']
['grey07', '2070', 'Laura', 'Grey', '35']
['johnson81', '4081', 'Craig', 'Johnson', '27']
['jenkins46', '9346', 'Mary', 'Jenkins', '48']
['smith79', '5079', 'Jamie', 'Smith', '63']
"""
print()


########################################################################################################################

""" UŻYCIE DICTREADERA"""

"""
Teraz zamiast READERA wprowadzamy DICTREADERA.

DictReader całą zawartość zmienia w słownik. 
Jeżeli dopiszemy więcej lub mniej nazw kolumn, to pojawi się "None"
"""

with open(filename, encoding='utf-8', newline='') as user_file:
    reader = csv.DictReader(user_file, delimiter=';')

    for row in reader:
        print(row)
"""
Wynik: 
{'Username': 'booker12', 'Identifier': '9012', 'First name': 'Rachel', 'Last name': 'Booker', 'Age': '44'}
{'Username': 'grey07', 'Identifier': '2070', 'First name': 'Laura', 'Last name': 'Grey', 'Age': '35'}
{'Username': 'johnson81', 'Identifier': '4081', 'First name': 'Craig', 'Last name': 'Johnson', 'Age': '27'}
{'Username': 'jenkins46', 'Identifier': '9346', 'First name': 'Mary', 'Last name': 'Jenkins', 'Age': '48'}
{'Username': 'smith79', 'Identifier': '5079', 'First name': 'Jamie', 'Last name': 'Smith', 'Age': '63'}
"""

"""
W tym momencie dane to słownik. Nie musimy usuwać ręcznie pierwszej linijki danych, która zawiera nagłówki kolumn (headers). 
DictReader automatycznie będzie traktował wiersz z nazwami kolumn jako informację o kluczach dla wartości w mapie (słowniku). 
DictReader przekształca dane w słownik. 
"""
print()


########################################################################################################################

""" NADANIE WŁASNYCH NAGŁÓWKÓW KOLUMN W DICTREADERZE """
"""
W domyślnyn podejściu DictReader traktuje pierwszą linię (pierwszy wiersz) jako klucze do mapy. 
Pozwala również na to, jakie nagłówki kolumn chce użytkownik. 
"""


with open(filename, encoding='utf-8', newline='') as user_file:
    headers = ['jeden', 'dwa', 'trzy', 'cztery', 'piec']  # dodajemy nazwy kolumn
    reader = csv.DictReader(user_file, delimiter=';', fieldnames=headers)

    for row in reader:
        print(row)
"""
Wynik: 
{'jeden': 'Username', 'dwa': 'Identifier', 'trzy': 'First name', 'cztery': 'Last name', 'piec': 'Age'}
{'jeden': 'booker12', 'dwa': '9012', 'trzy': 'Rachel', 'cztery': 'Booker', 'piec': '44'}
{'jeden': 'grey07', 'dwa': '2070', 'trzy': 'Laura', 'cztery': 'Grey', 'piec': '35'}
{'jeden': 'johnson81', 'dwa': '4081', 'trzy': 'Craig', 'cztery': 'Johnson', 'piec': '27'}
{'jeden': 'jenkins46', 'dwa': '9346', 'trzy': 'Mary', 'cztery': 'Jenkins', 'piec': '48'}
{'jeden': 'smith79', 'dwa': '5079', 'trzy': 'Jamie', 'cztery': 'Smith', 'piec': '63'}
"""

"""
W tym przykładzie nazwaliśmy klucze jako ['jeden', 'dwa', 'trzy', 'cztery', piec']
Nasze klucze to headery. Minusem jest to, że pierwszy wiersz potraktowany jest teraz jako dane: 

    {'jeden': 'Username', 'dwa': 'Identifier', 'trzy': 'First name', 'cztery': 'Last name', 'piec': 'Age'}
    
DictReader pobiera informację, jakie wartości ma nadać kluczom w mapie, ale w tym wypadku pierwsza linia (tam, gdzie są
nazwy kolumn) potraktuje jak pierwszy wiersz z danymi. 

Rozwiązaniem jest przeczytanie pierwszej linii i pominięcie jej. 
"""
print()


########################################################################################################################

""" NIEZGODNOŚĆ NAZW KOLUMN Z LICZBĄ DANYCH """

"""
W przypadku zastosowania DictReadera, gdy pominiemy nazwę kolumny lub kolumn albo dodamy nadmiarowe nazwy kluczy, 
DictReader poradzi sobie sam. 
"""


with open(filename, encoding='utf-8', newline='') as user_file:
    headers = ['jeden', 'dwa', 'trzy', 'cztery', 'piec', 'blabla']  # dodajemy nadmiarową kolumnę
    reader = csv.DictReader(user_file, delimiter=';', fieldnames=headers)

    for row in reader:
        print(row)
"""
Wynik: 
{'jeden': 'Username', 'dwa': 'Identifier', 'trzy': 'First name', 'cztery': 'Last name', 'piec': 'Age', 'blabla': None}
{'jeden': 'booker12', 'dwa': '9012', 'trzy': 'Rachel', 'cztery': 'Booker', 'piec': '44', 'blabla': None}
{'jeden': 'grey07', 'dwa': '2070', 'trzy': 'Laura', 'cztery': 'Grey', 'piec': '35', 'blabla': None}
{'jeden': 'johnson81', 'dwa': '4081', 'trzy': 'Craig', 'cztery': 'Johnson', 'piec': '27', 'blabla': None}
{'jeden': 'jenkins46', 'dwa': '9346', 'trzy': 'Mary', 'cztery': 'Jenkins', 'piec': '48', 'blabla': None}
{'jeden': 'smith79', 'dwa': '5079', 'trzy': 'Jamie', 'cztery': 'Smith', 'piec': '63', 'blabla': None}
"""
print()
"""
Kiedy dodamy za dużo nazw kolumn w stosunku do rzeczywistych danych, wówczas DictReader weźmie nadmiarowe kolumny jako 
klucze, a w miejsce ich wartości podstawi wartości domyślną 'None' --> 'blabla': None
"""


with open(filename, encoding='utf-8', newline='') as user_file:
    headers = ['jeden', 'dwa', 'trzy', 'cztery']  # podajemy za mało nazw kolumn
    reader = csv.DictReader(user_file, delimiter=';', fieldnames=headers)

    for row in reader:
        print(row)
"""
Wynik: 
{'jeden': 'Username', 'dwa': 'Identifier', 'trzy': 'First name', 'cztery': 'Last name', None: ['Age']}
{'jeden': 'booker12', 'dwa': '9012', 'trzy': 'Rachel', 'cztery': 'Booker', None: ['44']}
{'jeden': 'grey07', 'dwa': '2070', 'trzy': 'Laura', 'cztery': 'Grey', None: ['35']}
{'jeden': 'johnson81', 'dwa': '4081', 'trzy': 'Craig', 'cztery': 'Johnson', None: ['27']}
{'jeden': 'jenkins46', 'dwa': '9346', 'trzy': 'Mary', 'cztery': 'Jenkins', None: ['48']}
{'jeden': 'smith79', 'dwa': '5079', 'trzy': 'Jamie', 'cztery': 'Smith', None: ['63']}
"""
print()
"""
Piąta nazwa kolumny jest dodana jako klucz 'None' --> None: ['Age']
W przypadku, gdyby brakowało więcej nazw kolumn, wówczas DictReader zacznie przekształcać dane (wartości) dla brakujących 
nazw kluczy na listy, np. None: ['First name', 'Last name', 'Age'].
"""


with open(filename, encoding='utf-8', newline='') as user_file:
    headers = ['jeden', 'dwa']  # podajemy za mało nazw kolumn
    reader = csv.DictReader(user_file, delimiter=';', fieldnames=headers)

    for row in reader:
        print(row)
"""
Wynik: 
{'jeden': 'Username', 'dwa': 'Identifier', None: ['First name', 'Last name', 'Age']}
{'jeden': 'booker12', 'dwa': '9012', None: ['Rachel', 'Booker', '44']}
{'jeden': 'grey07', 'dwa': '2070', None: ['Laura', 'Grey', '35']}
{'jeden': 'johnson81', 'dwa': '4081', None: ['Craig', 'Johnson', '27']}
{'jeden': 'jenkins46', 'dwa': '9346', None: ['Mary', 'Jenkins', '48']}
{'jeden': 'smith79', 'dwa': '5079', None: ['Jamie', 'Smith', '63']}
"""
print()


########################################################################################################################

""" DIALEKT """

"""
Moduł csv posiada wbudowany gotowy dialekt 'excel'. Python wie, że dialekt 'excel' to ten, w którym operuje się na 
plikach csv. 

Jeśli wejdziemy 'ctrl + B' widać, że: 

    class excel(Dialect):
        '''Describe the usual properties of Excel-generated CSV files'''.
        delimiter = ','
        quotechar = '"'
        doublequote = True
        skipinitialspace = False
        lineterminator = '\r\n'
     quoting = QUOTE_MINIMAL
    register_dialect("excel", excel)
    
Doskonale widać, że naszym podzielnikiem jest PRZECINEK, nowa linia to '\r\n'. 
"""

our_dialect = csv.excel
our_dialect.delimiter = ';'  # możemy zastosować inny rozdzielnik (delimiter) z przecinka na średnik czy pipe.

with open(filename, encoding='utf-8', newline='') as user_file:
    headers = ['jeden', 'dwa', 'trzy', 'cztery', 'piec']  # dodajemy nazwy kolumn
    reader = csv.DictReader(user_file, dialect=our_dialect, fieldnames=headers)  # rezygnujemy z rozdzielnika

    for row in reader:
        print(row)