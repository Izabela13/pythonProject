""" WPROWADZENIE DICT READERA """

import csv


"""
Plik, na którym pracujemy, ma rozszerzenie 'txt'. Rozszerzenie 'txt' podpowiada systemiowi, aby domyślnie otworzyć plik 
w notatniku. Struktura pliku w środku jest taka sama.   
"""

filename = 'country_info.txt'
countries_dict = {}  # mapa krajów

"""
Dodanie dialektu i ustawienie delimitera na pipe ('|') --> kraje rozdzielane są tym właśnie znakiem
"""
dialect = csv.excel
dialect.delimiter = '|'


"""
1. Wyciąganie nagłówków kolumn z pliku (headers) 
    headers = country_file.readline().rstrip('\n').split(dialect.delimiter)
Plik zapisany jako "country_file" będzie miał: 
a) przeczytaną pierwszą linię - readline()
b) usuniety znak nowej linii - rstrip('\n')
c) poszczególne nazwy kolumn rozdzielone według "dialekt.delimiter", czyli pipem ('|')

Dla nagłówków kolumn (headersów) stosujemy metodę 'casefold()', która spowoduje, że nazwy kolumn będą zamienione na
małe litery. Zastosowanie metody casefold() w pętli. 


2. Tworzenie readera, a dokładnie - DictReadera.
Do DictReadera przekazujemy plik "country_file", czyli ten, do którego odczytujemy ('r' jest domyślne).
Przekazany dialekt.

Musimy też przekazać, że pierwsza linijka danych to headery --> fieldnames=headers. 
Nagłówki kolumn zostały odczytane wcześniej. Jeżeli nie podamy fieldnames, to DictReader potraktuje kolejną po 
przeczytanej linii jako headery. DictReaderowi trzeba wskazać, że nagłówki kolumn znajdują się w zmiennej "headers".
Nagłówki kolumn zostały przeprocesowane tak, aby zawierały w nazwie tylko małe litery. 

3. Iterowanie po każdym wierszu w readerze.
Do mapy "countries_dict" można wstawić teraz dane. 
    countries_dict[row['country'].casefold()] = row
Klucze w mapie muszą być z małej litery --> dodanie 'casefold()'
"""


with open(filename, encoding='utf-8', newline='') as country_file:
    headers = country_file.readline().rstrip('\n').split(dialect.delimiter)

    for index, header in enumerate(headers):
        headers[index] = header.casefold()  # przekształcanie wszystkich headerów na pisane małymi literami.

    #Tworzenie readera, któremu zosatnie przekazany plik
    reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headers, delimiter='|')

    for row in reader:
        countries_dict[row['country'].casefold()] = row  # klucze muszą być z małej litery
        countries_dict[row['cc'].casefold()] = row


while True:
    selected_country = input("Podaj kraj lub kod: ")
    if selected_country == "":
        break

    result = countries_dict.get(selected_country.casefold())
    if result:
        print(f"Stolica: {result['capital']}",
              f"Strefa czasowa: {result['timezone']}"
              f"Kod kierunkowy: {result['iac']}",
              f"Waluta: {result['currency']}",
              sep='\n\t')
        print("")
    else:
        print(f"Nie ma takiego klucza jak {selected_country} \n")