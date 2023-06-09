""" RÓŻNICA MIĘDZY FUNKCJĄ WRITE() A PRINT() """

test_numbers = 'numbers.txt'

# with open(test_numbers, 'w', encoding='utf-8') as numbers_file:
#     for i in range(10):
#         print(i, file=number_file)  # print() zapisuje do stringa

"""
Po wykonaniu instrukcji pojawi się nowy plik 'numbers.txt', w którym znajdą się jedna pod drugą cyfry od 0 do 9. 
Jeżeli funkcja print() zostanie zamieniona przez funkcję write(), pojawi się wyjątek:
    TypeError: write() argument must be str, not int
Funkcja write() zapisuje do stringa. Nie można wstawić do niej wartości int.  
"""

# with open(test_numbers, 'w', encoding='utf-8') as numbers_file:
#     for i in range(10):
#         numbers_file.write(i)

"""
Od razu trzeba przerzutować liczby do stringa.
Funkcja "write()" przyjmuje tylko jeden argument. 
W funkcji print() można dać jakiś separator. 

Użycie print() i write() zależy od potrzeb. 
"""

# with open(test_numbers, 'w', encoding='utf-8') as numbers_file:
#     for i in range(10):
#         numbers_file.write(str(i))  # rzutowanie liczby do stringa

"""
W pliku 'numbers.txt' pojawi się zapis: 0123456789
Funkcja write() domyślnie zapisuje wszystkie elementy w jednej linii. 
"""

"""
Kiedy używać write() a kiedy używać print() do zapisu plików? 
Wszystko zależy od zapotrzebowania. Print() jest elastyczniejszy - pozwoli na przekazanie więcej niż jednego argumentu.
"""

with open(test_numbers, 'w', encoding='utf-8') as numbers_file:
    for i in range(10):
        print(i, 'funkcja print jest super', file=numbers_file)
"""
Wynik: 
0 funkcja print jest super
1 funkcja print jest super
2 funkcja print jest super
3 funkcja print jest super
4 funkcja print jest super
5 funkcja print jest super
6 funkcja print jest super
7 funkcja print jest super
8 funkcja print jest super
9 funkcja print jest super
"""

"""
Dodatkowo w funkcji print() można dodać separator
"""


with open(test_numbers, 'w', encoding='utf-8') as numbers_file:
    for i in range(10):
        print(i, 'funkcja print jest super', file=numbers_file, sep='\t\t\t')