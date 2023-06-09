""" Zapisywanie do pliku """

animals_array = [
    "Kot - Ssak",
    "Pies - Ssak",
    "Wąż - Gad",
    "Dziobak - Ssak"
    "Sowa - Ptak",
    "Komodo - Gad",
    "Szerszeń - Owad",
    "Tarantula - Gad",
    "Żaba - Płaz",
    "Miś - Ssak",
    "Koń - Ssak",
    "Pszczoła - Owad",
    "Kukułka - Ptak",
    "Mucha - Owad", ]

""" 
Nadawanie nazwy plikowi, do którego chcemy coś zapisać. 
Działania będą podobne, jak przy odczytywaniu: 
1. Otworzyć plik. Jeśli plik nie istnieje trzeba go otworzyć w odpowiednim trybie, aby się utworzył. 
2. Zapisywanie/ zrzucanie wszystkich danych do pliku.
3. Zamykanie pliku. 
"""

animals_filename = 'animals.txt'

"""
Żeby otworzyć plik na serwerze nieprodukcyjnym wystarczy użyć składni: 
WITH OPEN () AS

Zapisywanie jest analogiczne jak otwieranie pliku. Potrzebne są trzy argumenty: 
- nazwa zmiennej, do jakiej został przypisany plik, np. zmienna 'animals_filename'
- mode = 'w'
- encoding='utf-8'

Jeżeli chcemy zapisywać coś do pliku, nie możemy użyć argumentu 'r' ('read'). 
Zamiast argumentu 'r' używa się argumentu 'w' ('write').  

Po 'AS' nadajemy nazwę dla pliku, na której to nazwie będziemy działać.
"""

with open(animals_filename, 'w', encoding='utf-8') as animals:
    for animal in animals_array:  # iterowanie po liście zwierząt
        print(animal, file=animals)  # print to nie jedyna metoda, jaka zapisuje do pliku

"""
Po wykonaniu powyższej instrukcji, w folderze, w którym mamy pliki (np. jak w tym wypadku '4. write_file' utworzy się
nowy plik o przekazanej nazwie - w tym wypadku 'animals.txt'. Plik ten będzie pusty, ponieważ na tym etapie jeszcze nic
nie zostało do niego zapisane. 

Żeby zapisać coś do pliku można użyć funkcji print().
Funkcja print() ma wiele zastosowań, np. 
- defaultowo służy do tego, aby coś wydrukować na konsolę
- dodaje znak nowej linii
Aby funkcja print() zapisała coś do pliku, trzeba dodać w jej ciele dodatkowy argument - 'file=nazwa_tablicy'. 
Po dodaniu argumentu 'file' lista zwierząt zostanie zapisana do pliku animals.txt

Jeżeli przyjrzymy się plikowi 'animals.txt', to z łatwością dostrzeżemy, że poszczególne elementy listy znajdują się 
w nowej linii. Funkcja print() dodała każdemu elementowi znak nowej linii. 
Jeżeli chcemy mieć wszystkie elementy w jednej linii, wówczas trzeba dodać argument 'end' i zanzaczyć: end=''. 
"""

"""
W folderze, w którym zapisujemy pliki pod wskazaną nazwą, plik zawsze będzie jeden, niezależnie od tego, ile razy 
zostanie do niego coś zapisane. 

Tryb zapisu, czyli 'w' działa w ten sposób: 
--> Jeżeli pliku nie ma, to go utwórz i zapisz do niego. 
--> Jeśli plik już istnieje, to usuń wszystko, co w nim jest i zacznij go zapisywać od nowa (nadpisz). 
"""

"""
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

Tryby: 

Character   Meaning
'r'         open for reading (default)
'w'         open for writing, truncating the file first
'x'         open for exclusive creation, failing if the file already exists
'a'         open for writing, appending to the end of file if exists
'b'         binary mode
't'         text mode (default)
'+'         open for updating (reading and writing)
"""

"""
Funkcja print() to nie jedyny sposób na zapisywanie do pliku. 
Metoda write() to drugi sposób. Metoda write() wypisuje wszystkie dane w jendej linii. 
--> metoda write() działa jak funkcja print(end=''). 
"""

with open(animals_filename, 'w', encoding='utf-8') as animals:
    for animal in animals_array:
        animals.write(animal)

"""
Różnica między PRINT() a WRITE()
1. Funkcja write() zapisuje wszystko 'tak jak jest', czyli tak, jak zostanie przekazane do tej funkcji. 
2. Print() domyślnie pod spodem wszystko zamienia na string (reprezentację stringową).   
"""