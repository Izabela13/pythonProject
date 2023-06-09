""" ODCZYTYWANIE PLIKÓW CSV """

"""
Moduł csv jest wbudowany w Python i pozwala w łatwy sposób operaować na plikach csv.
"""

import csv

# Na początku zapisywanie nazwy pliku do zmiennej 'filename'
filename = 'username.csv'


########################################################################################################################

""" OTWIERANIE PLIKU CSV I DODANIE READERA """

# with open(filename, encoding='utf-8', newline='') as csv_file:  # nadanie nazwy
#     reader = csv.reader(csv_file, delimiter=";")
#     for row in reader:
#         print(row)
"""
Wynik: 
['Username', 'Identifier', 'First name', 'Last name', 'Age']
['booker12', '9012', 'Rachel', 'Booker', '44']
['grey07', '2070', 'Laura', 'Grey', '35']
['johnson81', '4081', 'Craig', 'Johnson', '27']
['jenkins46', '9346', 'Mary', 'Jenkins', '48']
['smith79', '5079', 'Jamie', 'Smith', '63']
"""

"""
Parametr "newline" potrzebuje informacji, jaki charakter/znak jest tym charakterem/znakiem nowej linii. 
Parametr nowej linii podany jest jako pusty. Chodzi o to, że moduł "csv" jest zaimplementowany w ten sposób, że jeżeli 
my nie przekażemy parametru nowej linii, to moduł automatycznie wydedukuje jaki jest znak nowej linii. 
Zalecane jest zostawienie newline jako pustego ciągu znaków --> newline = ''. 
Biblioteka csv ma zaimplementowane automatyczne rozpoznanie nowej linii. 
"""


"""
W porównaniu do wcześniejszego otwierania plików, teraz następują zmiany. 

W ciele bloku 'with open as' tworzony jest READER (obiekt/ metoda do otwierania plików csv) z biblioteki csv. 
W metodzie 'reader()' trzeba podać: 
-> jaki plik (tutaj jest to plik 'csv_file', który został otwarty) 
-> czym dane są rozdzielone (tutaj jest to średnik --> delimiter=";"). 

Reader jest obiektem iterowalnym. Można wykonać na nim pętlę for (daj nam wiersze w naszym readerze).
Reader dzieli dane po średniku i zamienia od razu w listy (każda linijka to teraz lista).
"""


########################################################################################################################

""" POZBYWANIE SIĘ NAGŁÓWKÓW KOLUMN - METODA READLINE """

"""
W pliku pierwszy wiersz to zazwyczaj nazwy kolumn (które nie zawsze powinny zostać odczytane). 
Zanim 'reader' zostanie utworzony, zostanie przekazana instrukcja, co zrobić z pierwszym wierszem (nazwami kolumn): 
headers = csv_file.readline().strip('\n').split(';')  # przypisanie instrukcji do zmiennej jest opcjonalne.

metoda READLINE(): 
'Przeczytaj jedną linię'.

metoda STRIP(): 
Do stripa można przekazać argument. 
Metoda 'strip' w swoim defaultowym działaniu czyści white spaces (białe znaki). 
Do metody 'strip' można przekazać, o jakie dokładnie charaktery/znaki nam chodzi. 

metoda SPLIT(): 
W przykładzie trzeba zwrócić uwagę, że nie jesteśmy w 'csv.reader'. Trzeba wykorzystać rozdzielenie elementów.
'splitujemu' po naszym 'delimiterze', czyli w tym przykładzie po średniku.

Po zastosowaniu tych trzech metod, na kosoli nie zostaną wyświetlone headery (nazwy kolumn). 
"""

# with open(filename, encoding='utf-8', newline='') as csv_file:
#     headers = csv_file.readline().strip('\n').split(';')  # plik, który został otwarty
#     reader = csv.reader(csv_file, delimiter=";")
#     for row in reader:
#         print(row)
"""
Wynik: 
['booker12', '9012', 'Rachel', 'Booker', '44']
['grey07', '2070', 'Laura', 'Grey', '35']
['johnson81', '4081', 'Craig', 'Johnson', '27']
['jenkins46', '9346', 'Mary', 'Jenkins', '48']
['smith79', '5079', 'Jamie', 'Smith', '63']
"""

"""
Metoda "readline" w czasie iteracji otwartego pliku czyta pierwszą linię i idzie dalej. 
W momencie tworzenia readera, reader wie, że ma zacząć od drugiej linii. Iteracja zaczyna się od drugiej linii.
Odczytanie pierwszej linii i pominięcie jej w iteracji nie musi być przypisywane do żadnej zmiennej. 

Metoda "strip()" dzieli linie

Wszystkie obiekty, które pojawiły się na konsoli są teraz stringami. W tym przykładzie dwie kategorie, tj. numer id oraz
wiek, powinny być intami (liczbami całkowitymi). 
Moduł csv pomaga sobie z tym poradzić, ale jeśli pewien warunek jest spełniony.
Warunkiem musi być to, że wszystkie stringi są faktycznie przedstawione jako stringi (oplecione podwójnym apostrofem "")
"""


########################################################################################################################

""" ZACHOWANIE CHARAKTERU LICZB PRZY OTWIERANIU PLIKU CSV"""

"""
Do readera zostanie dodany kolejny parametr nazwany, który pozwoli na zachowanie liczb całkowitych lub zmiennoprzecinkowych
jako liczb. Ten parametr to 'quoting'.
"""

# with open(filename, encoding='utf-8', newline='') as csv_file:
#     csv_file.readline().strip('\n').split(';')  # zmienną "headers" można usunąć.
#     reader = csv.reader(csv_file, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
#     for row in reader:
#         print(row)
"""
Wynik: 
['booker12', 9012.0, 'Rachel', 'Booker', 44.0]
['grey07', 2070.0, 'Laura', 'Grey', 35.0]
['johnson81', 4081.0, 'Craig', 'Johnson', 27.0]
['jenkins46', 9346.0, 'Mary', 'Jenkins', 48.0]
['smith79', 5079.0, 'Jamie', 'Smith', 63.0]
"""

"""
quoting = csv.QUOTE_NONNUMERIC --> przekazanie readerowi, że wszystkie liczby są poza apostrofami.
--> stringi traktuj jako stringi ""
--> liczby traktuj jako liczby

Minusem tego rozwiązania jest to, że liczby nie są intami (liczba całkowitymi), tylko zmiennoprzecinkowymi. 
Potem można rzutować te typy. 
"""

"""
Co się stanie, gdy string w pliku źródłowym nie będzie owinięty w podwójne apostrofy?
Plik się nie odczyta. Pojawi się wyjątek, np.: ValueError: could not convert string to float: 'booker12'.
"""


########################################################################################################################

""" TWORZENIE SNIFFERA """

"""
Może się zdarzyć, że nie będzie wiadomo, czym rozdzielane są dane w jakimś pliku. 
W tym wypadku nie wiadomo, co wpisać w pozycję 'delimiter'. 
"W Pythynie nie ma problemów, są tylko wyzwania". 

W module csv istnieje klasa SNIFFER. Sniffer - jak sama nazwa wskazuje - "niucha", czym jest delimiter. 

Aby Sniffer zadziałał, potrzebuje on jakiejś próbki danych --> sample = csv_file.read().
Metoda read() przeczyta cały plik jako jeden wielki string. Na tej podstawie Sniffer może "wyniuchać" dialekt danych.

Poza metodą "readline" jest metoda "readlines". Ta metoda czyta wszystkie linie i trzyma je w liście.
Jeżeli wyjdziemy z bloku 'with open' i wyprintujemy na konsolę zawartość 'readlines', powinniśmy mieć dostęp do całości.
"""

# with open(filename, encoding='utf-8', newline='') as csv_file:
#     csv_file.readline().strip('\n').split(';')

    # # Sniffer
    # sample = csv_file.read()
    # file_dialect = csv.Sniffer().sniff(sample)

    # # przekazujemy dialekt, który został znaleziony przez Sniffera
    # reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC, dialect=file_dialect)

    # for row in reader:
    #     print(row)
"""
Na konsoli nie wyświetli się nic, chociaż Sniffer zadziałał poprawnie. 
Przeczytaliśmy cały plik. Sniffer przeczytał wszystko tak jak jest i właściwie już nic nie zostało do iterowania. 
Sniffer wydedukował, jaki jest dialekt w pliku, ale kursor znajduje się na końcu pliku. 

Teraz trzeba wrócić na początek pliku - zacząć odczytywać dane. 
Do tego służy metoda 'SEEK'. Do metody 'SEEK' przekazujemy OFFSET - jaki offset ma zastosować do poszukiwań. 
W tym przykładzie do offsetu wpisujemy '0' --> seek(0). 
"""


# with open(filename, encoding='utf-8', newline='') as csv_file:
#     csv_file.readline().strip('\n').split(';')  # Headery nie muszą być przypisane do żadnej zmiennej.

    # # Sniffer
    # sample = csv_file.read()  # metoda read przeczyta tekst (plik) jako cały string
    # file_dialect = csv.Sniffer().sniff(sample)  # wywąchiwanie dialektu. Sniffer potrzebuje jakiejś próbki (sample).

    # # Wracamy do początku pliku
    # csv_file.seek(0)  # nie mamy możliwości poruszania się po liniach innych niż iterowalne
    # csv_file.readline().strip('\n').split(file_dialect.delimiter)

    # # przekazanie "dialekt", który został znaleziony przez Sniffer
    # reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC, dialect=file_dialect)  # nie wpisujemy delimitera

    # # Można teraz dokonać iteracji po liniach (wierszach)
    # for row in reader:
    #     print(row)
"""
Wynik:
['booker12', 9012.0, 'Rachel', 'Booker', 44.0]
['grey07', 2070.0, 'Laura', 'Grey', 35.0]
['johnson81', 4081.0, 'Craig', 'Johnson', 27.0]
['jenkins46', 9346.0, 'Mary', 'Jenkins', 48.0]
['smith79', 5079.0, 'Jamie', 'Smith', 63.0]
"""

"""
Po powrocie na początek: 
    csv_file.seek(0)  
 
trzeba dodać jeszcze usuwaie nagłówków kolumn: 
    csv_file.readline().strip('\n').split(file_dialect.delimiter)
    
Do Sniffera można dodać nagłówki kolumn, ponieważ one też są częścią danych
"""


with open(filename, encoding='utf-8', newline='') as csv_file:

    # Sniffer
    sample = csv_file.read()  # metoda read przeczyta tekst jako cały string
    file_dialect = csv.Sniffer().sniff(sample)  # Sniff zwraca obiekt

    # Wracamy do początku pliku
    csv_file.seek(0)  # nie mamy możliwości poruszania się po liniach innych niż iterowalne
    csv_file.readline().strip('\n').split(file_dialect.delimiter)  # w split podajemy wyniuchany delimiter

    # przekazanie "dialekt", który został znaleziony przez Sniffer
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC, dialect=file_dialect)

    for row in reader:
        print(row)
"""
Wynik:
['booker12', 9012.0, 'Rachel', 'Booker', 44.0]
['grey07', 2070.0, 'Laura', 'Grey', 35.0]
['johnson81', 4081.0, 'Craig', 'Johnson', 27.0]
['jenkins46', 9346.0, 'Mary', 'Jenkins', 48.0]
['smith79', 5079.0, 'Jamie', 'Smith', 63.0]
"""

"""
Możemy się cofnąć do pierwszej linijki. Dajemy do 'seek' wartość '1' --> seek(1).
Generalnie na konsoli nic się nie pojawia. Niezależnie od tego, co wpiszemy w 'seek', wracamy za każdym razem 
na początek pliku. Nie ma możliwości poruszania się po liniach innych niż iterowalne. 
"""

"""
Czy moglibyśmy to wszystko zrobić wydajniej? 
Ile linijek potrzebuje Sniffer, aby 'wyniuchać' separator danych?

Np. piewsze 10 linijek. 
Jeżeli plik zawiera setki tysięcy rekordów, wówczas wydajniej jest wrócić z 10 linijek na poczatek, niż z końca całego 
pliku na początek. 

Na tym przykładzie nie ma to znaczenia, ponieważ plik źródłowy jest niewielki. 
"""
print()


########################################################################################################################

""" DELIMITER """

"""
Obiekt sniffer ma kilka swoich atrybutów. 
"""

print(f"Delimiter: {file_dialect.delimiter}")
print(f"Escape: {file_dialect.escapechar}")
print(f"Line terminator {file_dialect.lineterminator}")
print(f"Line terminator {repr(file_dialect.lineterminator)}")
"""
Delimiter: ;
Escape: None
Line terminator 

Line terminator '\r\n'


Delimiterem jest średnik. Wszystko się zgadza. 
Line terminator jest pusty. Tak naprawdę 'line terminator' jest, Sniffer go znalazł. Na konsoli nie jest to dobrze widoczne, 
ale jest to biały znak. 
Jeżeli chcielibyśmy wyświetlić surowy widok naszego stringa, musimy użyć funkcji 'REPR'. Wówczas zobaczymy, że naszym 
znakiem nowej linii jest  '\r\n'. 
"""

"""
Do zapamiętania: 
Readline - czytanie jednej linii
Readlines - czytanie wszystkich linii w danym pliku i przetrzymywanie ich w liście. 
"""