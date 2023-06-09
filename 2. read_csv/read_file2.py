"""
Plik przypominający csv
"""

"""
Plik 'country_info.txt' przypomina plik w formacie csv. Pierwszy wiersz to nazwy kolumn, kolejne wiersze to dane.
Poszczególne informacje danego wiersza oddzielone są pipe'ami (znakiem |).
"""


filename = 'country_info.txt'

"""
Na serwerze produkcyjnym otwiera się pliki z użyciem 'try... exception... finally...'.
Dla własnego użytku można wykorzystać blok 'with'.

Słowo kluczowe WITH. Jeżeli w bloku 'with' wystąpi jakiś błąd i są to obiekty, które mogą zostać zamknięte, to zostaną
one zamknięte automatycznie. 
"""

# with open(filename, encoding='utf-8') as country_file:  # defaultowo jest tu mode = 'r'
#     for row in country_file:  # ciało otwartego pliku - blok open
#         print(row)


# Woriwadzenie drugiej pętli poza blokiem 'with open'
# for row in country_file:
#     print(row)
# Po wprowadzeniu drugiej pętli na końcu pojawi się ValueError
"""
Traceback (most recent call last):
ValueError: I/O operation on closed file.

Plik został zamknięty, iteracja nie jest możliwa. 
Plik został zamknięty po wyjściu z bloku 'with open'
"""


"""
split - rozdzielanie tekstu

Na końcu będzie widoczny znak nowej linii '\n'.
Aby się go pozbyć wystarczy dodać metodę strip().
"""

with open(filename, encoding='utf-8') as country_file:
    for row in country_file:
        data = row.strip().split('|')
        print(data)