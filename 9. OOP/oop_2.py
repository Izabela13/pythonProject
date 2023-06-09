import oop

print(f"OOP_1 {__name__}")

"""
Wyprintuje się coś takiego: 

True
False
True
<oop.Dog object at 0x00000170262B2ED0>
<oop.Dog object at 0x00000170262B2C10>
<oop.Dog object at 0x00000170262B2ED0>
oop
OOP_1 __main__
"""

"""
Jeżeli importujemy jakiś moduł albo plik wykonywalny, on automatycznie cały się wykonuje. 
W tym wypadku, jeśli puszczamy to z pliku "oop.py", to nazwa jest "__main__". 
Natomiast, jeśli puścimy sobie skrypt z pliku "oop_2.py", to nazwa jest "oop". 
Nazwa jest taka, jak nazwany jest plik. 

Często w Pythonie robi się tak, że nie chcąć, żeby pewne fragmenty kodu się uruchomiły, wstawia się warunek: 
    
    if __name__ == '__main__': 
    ...
"Tylko wtedy, kiedy "name" równa się "main", to uruchom mi fragmenty kodu. W innym wypadku nie uruchamiaj. 
"""