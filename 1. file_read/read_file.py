""" ODCZYTYWANIE PLIKÓW """


"""
Jeżeli z jakiegoś pliku odczytywane są dane, istnieje ryzyko, że połączenie do tego pliku nie zostanie zamknięte.
Każde otwarte połączenie wpływa na działanie serwera.
"""

"""
Zaczynamy od odczytania pliku. Przypiszemy go do jakiejś zmiennej. 
Słowo kluczowe, którym odczytujemy pliki w Pythonie to po prostu "open". 
Słowo kluczowe "open" przyjmuje kilka argumentów. 

Pierwszym argumentem jest nazwa samego pliku.

W nazwie pliku chodzi o ścieżkę do tego pliku. Trzeba zwrócić uwagę na to, 
czy plik nie jest dostępny lokalnie. 

prawy przycisk myszy na pliku --> CopyPath/Reference... --> Absolute Path Ctrl+Shift+C

Trzeba zwrócić uwagę na backslashe.
C:/Kursy/Python/pythonProject/1. file_read/lor.txt
Wszystkie backslashe '/' trzeba zamienić na '/'. Ten znak '/' to znak specjalny. 
- Zaznaczamy znak, 
- dajemy ctrl+f --> otworzy się okienko "jaki znak ma być zastąpiony", 
- dajemy ctrl+r --> otworzy się okienko "na jaki znak zastąpić".
- naciskamy "Replace All"

Drugi argument to w jakim trybie chcemy otworzyć plik. 

'r' --> oznacza tryb odczytu 'read'
"""

# lord_of_the_rings = open('C:/Kursy/Python/pythonProject/1. file_read/lor.txt', 'r')

"""
Przekazywanie plików przez taką ścieżkę jest złym nawykiem. 
ŚCIEŻKA ABSOLUTNA posiada np. login
Po przekazaniu takiego zapisu do inne użytkownika, taki plik nie zostanie odnaleziony. 
Dlatego podaje się ŚCIEŻKĘ RELATYWNĄ pliku, zaczynając od katalogu, w którym się znajdujemy.
"""

# lord_of_the_rings = open('lor.txt', 'r')

"""
Ścieżki do pliku podaje się "NAWIGUJĄC SIĘ DO NICH", nawigując się od miejsca, w którym zaczynamy (w którym jest root)
W tym momencie, jeśli plik zostanie przeniesiony do innego miejsca, PyCharm zmieni ścieżkę do pliku.

Plik typu: 
    lord_of_the_rings = open('lor.txt', 'r') 
jest iterowalny. 
"""

# for line in lord_of_the_rings:
#     print(line)

"""
Po wywołaniu pętli for pojawią się "dziwne" znaki zastępujące polskie znaki, czyli ś, ć, ż, ó, ł, ż
Dodatkowo zauważalne będą białe znaki reprezentowane przez dodatkowe linie:

    'Trzy PierĹ›cienie dla krĂłlĂłw elfĂłw pod otwartym niebem,

    Siedem dla wĹ‚adcĂłw krasnali w ich kamiennych paĹ‚acach,

    DziewiÄ™Ä‡ dla Ĺ›miertelnikĂłw, ludzi Ĺ›mierci podlegĹ‚ych,



    'Jeden dla WĹ‚adcy CiemnoĹ›ci na czarnym tronie

    W Krainie Mordor, gdzie zalegĹ‚y cienie,

    Jeden, by wszystkimi rzÄ…dziÄ‡, Jeden, by wszystkie odnaleĹşÄ‡,



    "Jeden", by wszystkie zgromadziÄ‡ i w ciemnoĹ›ci zwiÄ…zaÄ‡

    W Krainie Mordor, gdzie zalegĹ‚y cienie.





        - J.R.R. Tolkien, WĹ‚adca PierĹ›cieni
"""

"""
I. 
Jeżeli pliki otwierane są w taki sposób: 
    
    lord_of_the_rings = open('lor.txt', 'r')
    
zapominamy o tym, że plik trzeba zamknąć. Po całej operacji należy pamiętać o zamknięciu pliku:

    lord_of_the_rings.close()
    
Zamykanie plików jest szczególnie ważne na serwerach produkcyjnych. Każdy niezamknięty plik pozostaje w pamięci.
Po jakimś czasie może dojść do zapchania pamięci serwera produkcyjnego. 
"""

# lord_of_the_rings.close()


"""
II. 
Przy odczytywaniu pliku może się zdarzyć kilka sytuacji wyjątkowych. 
Trzeba dodać obsługe błędów.
"""


#######################################################################################################################

""" OBSŁUGA BŁĘDÓW - BLOK FINALLY """

# try:
#     lord_of_the_rings = open('lor.txt', 'r')  # ctrl + f - znajdź wszystkie znaki i zamień na inny

#     for line in lord_of_the_rings:
#         print(line)
#         raise ValueError  # Rzucenie błędem - po pierwszej linii coś się stało
# except Exception:  # Generalnie samo 'Exception' to zbyt ogólny błąd
#     print("EXCEPTION!!!")
# finally:  # W tym bloku powinno znaleźć się zamykanie plików
#     print(">>>>ZAWSZE SIĘ WYKONA<<<<")  # Niezależnie od tego, czy wystąpi sytuacja wyjątkowa, plik zostanie zamknięty.

# print("Będę zamykał plik")
# lord_of_the_rings.close()

"""
Pierwsza linia zostanie wyprintowana. 
Potem pojawi się wyjątek, czyli to, co sami wprowadziliśmy (raise ValueError).

    'Trzy PierĹ›cienie dla krĂłlĂłw elfĂłw pod otwartym niebem,

    EXCEPTION!!!
    >>>>ZAWSZE SIĘ WYKONA<<<<
    Będę zamykał plik
    
W tym wypadku program się zamknął. Gdyby zamykanie pliku było w metodzie, wówczas blok exception wykluczyłby zamknięcie.
"""

# try:
#     lord_of_the_rings = open('lor.txt', 'r')

    # for line in lord_of_the_rings:
    #     print(line)
    #     raise ValueError # Rzucenie błędem

    # print("Będę zamykał plik")
    # lord_of_the_rings.close()

# except Exception:
#     print("EXCEPTATION!!!")

# finally:
#     print(">>>>ZAWSZE SIĘ WYKONA <<<<")

"""
    'Trzy PierĹ›cienie dla krĂłlĂłw elfĂłw pod otwartym niebem,

    EXCEPTATION!!!
    >>>>ZAWSZE SIĘ WYKONA <<<<
    
Na konsoli nie pojawiło się "Będę zamykał plik". 
Interpreter nie dochodzi do tego fragmentu kodu, ponieważ napotkał linię kodu z 'raise ValueError'.
W tym momencie otwarte pliki zostają w systemie. 

Zamykanie pliku powinno znaleźć się w bloku 'finally'. Blok 'finally' wykonuje się zawsze.
"""

# try:
#     lord_of_the_rings = open('lor.txt', 'r')

#     for line in lord_of_the_rings:
#         print(line)
#         raise ValueError

# except Exception:
#     print("EXCEPTION!!!")

# finally:
#     print("Będę zamykał plik")
#     lord_of_the_rings.close()

"""
'Trzy PierĹ›cienie dla krĂłlĂłw elfĂłw pod otwartym niebem,

EXCEPTION!!!
Będę zamykał plik
"""


#######################################################################################################################

""" WHITE SPACES - BIAŁE ZNAKI """

"""
Otworzony plik 'lor.txt' prezentuje się zupełnie inaczej niż oryginał. 
Przy plikach tekstowych może to nie mieć większego znaczenia. Przy zestawieniu danych może prowadzić do niespójności.

white spaces, np.
- znak tabulacji 
- spacja, 
- znak końca linii

Na końcu linii w tekście oryginalnym występują znaki 'white spacecs' (właściwie znak końca linii). 
Nie widać tego w edytorze tekstowym, natomiast printuje się on na konsolę. 

Dodatkowo trzeba zwrócić uwagę na funkcję print(). Funkcja ta drukuje wszystko w nowej linii. Funkcja ta w swoim 
domyślnym zachowaniu ma zakodowane, że na końcu ciągu znaków ma kodować nową linijkę. 

Pierszy sposób na poradzenie sobie ze znakami nowej linii, to dodanie drugiego argumentu do funkcji print - end="".
Zostaną usunięte wolne linie pomiędzy kolejnymi liniami tekstu. Trzeba pamiętać, że nie pozbywamy się znaku białej linii
z końca wiersza. 
"""

# lord_of_the_rings = open('lor.txt', 'r')

# for line in lord_of_the_rings:
#     print(line, end="")
#     print(len(line))

# lord_of_the_rings.close()

"""
Sprawdzanie długości pierwszej linijki tekstu
"""

# text = "'Trzy Pierścienie dla królów elfów pod otwartym niebem,\n"
# print(len(text))
"""
Samych widocznych znaków jest: 48
Bez znaku nowej linii jest 55 znaków
Ze znakiem nowej linii jest 56 znaków. 

Dla nas znak nowej linii jest widoczny jako dwa znaki. Dla komputera jest to jeden znak. 
"""


#######################################################################################################################

""" STRIP"""

"""
Na ciągu znaków można wykonać metodę 'strip'.
Ta meteoda w swoim defaultowym działaniu będzie pozbywać się białych znaków z początku i z końca linii. 
"""

# lord_of_the_rings = open('lor.txt', 'r')

# for line in lord_of_the_rings:
#     print(line.strip(), end="")  # strip - pozbycie się znaków z początku i z końca linii

# lord_of_the_rings.close()

"""
Teraz tekst robi się jednolinijkowy. Winny jest temu end = ''. 
Wystarczy pozbyć się argumentu end=''. Funkcja print() domyślnie doda znak nowej linii na końcu linijki.
"""

# lord_of_the_rings = open('lor.txt', 'r')

# for line in lord_of_the_rings:
#     print(line.strip())

# lord_of_the_rings.close()

"""
Pozostaje tylko problem polskich liter. 

Program idzie linia po linii
rstrip() i lstrip() - stripowanie z prawej i z lewej strony naszego stringa
Nie można powiedzieć, że 'lstrip' to stripowanie z początku linii, a 'rstrip' z końca linii, dlatego że istnieją języki,
gdzie pisze się od prawej do lewej strony. 
"""


#######################################################################################################################

""" UTF-8 """

"""
Nasz oryginalny plik tekstowy zakodowany jest w UTF-8.

Na początku działania komputerów piewrsze znaki kodowane były w ASCII.
Kodowanie w ASCII - 128 znaków - znaki kodowane na 8 bitach. Obejmuje tylko alfabet amerykański
UTF-8 - kodowanie umożliwiające ujęcie wszystkich znaków świata (kodowanie znaku na czterech bajtach).

Do odczytu trzeba dodać kolejny argument - 'encoding'. W tym momencie można jawnie podać, jak kodowany jest plik.
"""

lord_of_the_rings = open('lor.txt', 'r', encoding='utf-8')  # 'r' - parametr - chcemy otworzyć w trybie do ODCZYTU

for line in lord_of_the_rings:
    print(line.strip())

lord_of_the_rings.close()

"""
Program został przeprocesowany w sposób prawidłowy.
Nastąpiło zamknięcie pliku po odczycie. 

Domyśla wartość dla pliku oryginalnego to UTF-8. Mimo to funkcja print() nie jest  w stanie wyświetlić go poprawnie. 
Sama funkcja print() również domyślnie odczytuje plik w kodowaniu UTF-8. 

W informatyce istnieje takie pojęcie jak DEFENSYWNE PROGRAMOWANIE. Można powiedzieć, że w tym przypadku jest to sposób
na zabezpieczenie się, aby program działał tak, jak powinien i korzystał z konkretnego rodzaju kodowania. 


Defaultowe kodowanie jest zależne od platformy, na której uruchamiany jest kod. 
"""