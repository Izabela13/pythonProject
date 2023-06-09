""" OTWIERANIE PLIKU DO ODCZYTU I JEDNOCZESNEGO ZAPISU """

import csv

"""
Na początku import modułu 'csv'

Chcemy przekształcić plik csv w zalążek gotowego programu w Pythonie. 
"""

ordering = ['athlete', 'gold', 'silver', 'bronze', 'country']

read_file_name = 'athlete_medals.csv'  # odczytujemy plik, który nazywa się 'athlete_medals.csv'
output_file_name = 'medals_dict.py'


with open(read_file_name, encoding='utf-8', newline='') as data, \
     open(output_file_name, 'w', encoding='utf-8') as output_file:

    print('import csv', file=output_file)  # zrzucanie danych do pliku 'output_file'
    print(file=output_file)  # zrzucamy pustą linię do pliku 'output_file'. Przekazujemy tylko znak nowej linii
    print('medals_table = [', file=output_file)  # otwieramy listę, czyli przypisujemy znak '['.

    reader = csv.DictReader(data)  # Tworzymy DictReadera, który będzie odczytywał nasze dane (medale)
    # nie musimy podawać delimitera, ponieważ wartością domyślną jest przecinek. Akurat nasze dane separowane są przez ,

    # ITERACJA PO WIERSZACH.
    for row_dict in reader:  # nazywamy 'row_dict', ponieważ każdy nasz wiersz jest mapą (słownikiem).
        new_dict = {}  # przelewamy dane do innego kubeczka. Chcemy też dodać inną kolejność. Stąd dodajemy 'ordering'.
        for key in ordering:  # iterowanie po tabeli ordering = ['athlete', 'gold', 'silver', 'bronze', 'country']
            value = row_dict[key]  # tworzenie nowych kluczy w mapie: 'athlete', 'gold', 'silver', 'bronze', 'country'
            if value.isnumeric():  # jeżeli wartość jest numeryczna, to niech będzie 'int'
                value = int(value)
            new_dict[key.casefold()] = value  # do słownika wkładamy klucz
        new_dict['total'] = None  # Dodanie nowego klucza

        print(f'\t{new_dict},', file=output_file)  # nowy dict chcemy dołożyć do plików

    print(']', file=output_file)  # zamknięcie tablicy
    print(file=output_file)


"""
W odczycie 'with open' nie musimy podawać 'r' jeżeli chcemy mieć plik tylko do odczytu. 
Parametr 'r' jest parameterm domyślnym dla struktury 'with open() as'. 
Podajemy newline = '', ponieważ jest to plik csv i moduł sam rozczyta sobie, jaki jest znak następnej linii. 
Zapisujemy plik jako 'as data', co oznacza, że plik jest dla nas zasileniem (zasileniem naszego programu). 

Przy składni 'with' możemy swobodnie wstawić przecinek i wstawić kolejne 'open'.
Do outputu ('output_file_name') będziemy zapisywać dane. Na końcu nazwy pliku dajemy rozszerzenie 'py'. 

Rozszerzenie nie ma znaczenia. 

Przy zapisywaniu pliku (nasze drugie open) musimy wstawić parameter 'w', ponieważ to parametr 'r' jest domyślny. 
W drugim odczytcie TRYP ODCZYTYWANIA PLIKU TO WRITE, czyli tryb odczytywania pliku do zapisu. 

Jeśli w Pythonie chcemy przenieść część bloku kodu do nowej linii, wystarczy wstawić znak łamania linii, czyli samo \.

Po słowie kluczowym "with" można otworzyć wiele plików. W tym przykładzie otwieramy dwa pliki - jeden do odczytu, drugi 
do zapisu. Nie otwieramy pliku do odczytu i zapisu tego samego pliku żeby np. dopisać coś w ostatniej linii. 
W tym przykładzie otwieramy dwa osobne pliki. Z jednego będziemy odczytywali, a do drugiego będziemy coś zapisywali
(zrzucali dane). 
"""

"""
Po uruchomieniu części programu widać, że jakiś zarys programu tworzy się w nowym pliku, czyli 'medals_dict.py'. 
"""