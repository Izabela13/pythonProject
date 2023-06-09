""" ZAPISYWANIE DO PLIKU CSV """

import csv

cereals = [
    ["Barley", 556, 1.7, 32.9, 10.1, 13.8],
    ["Durum", 339, 5, 27.4, 4.09, 9.7],
    ["Fonio", 240, 1, 4, 1.7, 0.05],
    ["Maize", 442, 7.4, 37.45, 6.15, 11.03],
    ["Millet", 484, 2, 37.9, 13.4, 9.15],
    ["Oats", 231, 9.2, 35.1, 10.3, 3.73],
    ["Rice (Brown)", 346, 2.8, 38.1, 9.9, 0.8],
    ["Rice, (White)", 345, 3.6, 37.6, 5.4, 0.1],
    ["Rye", 422, 2, 31.4, 18.2, 21.2],
    ["Sorghum", 316, 3, 37.8, 9.92, 9.15],
    ["Triticale", 338, 1.81, 36.6, 19, 0.9],
    ["Wheat", 407, 1.2, 27.8, 12.9, 13.8],
]

# Nazwy kolumn to osobna lista. Nie są częścią danych samych w sobie.
column_headings = ["Cereal", "Calories", "Fat", "Protein", "Fibre", "Vitamin E"]

filename = 'my_cereals.csv'

"""
Otwieramy plik do zapisu. Podajemy: 
- imię pliku ('filename')
- 'w' --> write (plik po otwarciu ma coś zapisać)
- encoding='utf-8' 
- newline='' --> parametr, dzięku któremu moduł csv sam sobie wydedukuje, jaki jest znak nowej linii w pliku
"""

"""
Podobnie jak wcześniej tworzony był obiekt 'READER', teraz tworzony będzie obiekt 'WRITER'. 
Do writera podajemy: 
- nazwę pliku ('output_file', czyli plik, który zapisaliśmy pod tą nazwą) --> Zapisz mi do mojego pliku wyjściowego
- 
Zapisujemy teraz wszystkie wiersze naszej listy do pliku. 

Przy odczycie danych iterowaliśmy po kolejnych danych w naszej liście i funkcją print() lub funkcją write() 
zapisywaliśmy dane do pliku. 

Na obiekcie writer mamy taką metodę jak 'writerows'. Ta metoda będzie oczekiwała jakieś obiektu iterowalnego. 
"""

with open(filename, 'w', encoding='utf-8', newline='') as output_file:
    writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC)  # zapisz do pliku wyjściowego
    writer.writerows(cereals)

"""
Po uruchomieniu programu dane, które mamy w tym skrypcie zapiszą się do pliku 'my_cereals.csv'.

Nowy plik będzie zawierał taki oto zestaw danych: 
"Barley",556,1.7,32.9,10.1,13.8
"Durum",339,5,27.4,4.09,9.7
"Fonio",240,1,4,1.7,0.05
"Maize",442,7.4,37.45,6.15,11.03
"Millet",484,2,37.9,13.4,9.15
"Oats",231,9.2,35.1,10.3,3.73
"Rice (Brown)",346,2.8,38.1,9.9,0.8
"Rice, (White)",345,3.6,37.6,5.4,0.1
"Rye",422,2,31.4,18.2,21.2
"Sorghum",316,3,37.8,9.92,9.15
"Triticale",338,1.81,36.6,19,0.9
"Wheat",407,1.2,27.8,12.9,13.8
"""

"""
Trzeba pamiętać, że obiekty, które mają być traktowane jako stringi, były ujęte w podwójne apostrofy. 
Osoba, która będzie odczytywać dane będzie mogła użyć 'quotingu', czyli: quoting=csv.QUOTE_NONNUMERIC

Na co jeszcze zwrócić uwage: 
1. Defaltowo obiekt 'writer' rozdziela dane przecinkami. Widać to po wyświetleniu danych.

2. Jeśli w obiekcie 'writer' zostawimy samo writer = csv.writer(output_file), wówczas nie będzie rozróżnienia na dane
tekstowe i liczbowe. Przez to przy odczycie w drugą stronę mogą pojawić się jakieś problemy. 

3. Jeśli nie użyjemy 'quotingu' przy zapisie, to możemy zauważyć, że: 
    "Rice, (White)",345,3.6,37.6,5.4,0.1
jest owinięte w podwójne apostrofy, a reszta 'stringów' nie. Wynika to stąd, że w nazwie 'Rice, (White)' występuje 
PRZECINEK, przez co moduł sam wydedukował, że jest to 'string'. Gdyby moduł nie dokonał ujęcia w podwójne apostrofy, 
wówczas mielibyśmy o jedną kolumnę więcej w tych danych. 
"""