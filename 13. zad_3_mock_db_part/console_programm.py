"""
Napisz program konsolowy który:
1.	Podczas uruchomienia wczyta dane z pliku ingredients.csv i zachowa je w wybranej przez siebie strukturze danych
2.	Po uruchomieniu w konsoli wyświetli menu z 4 możliwościami
    1 – Dodanie nowego składnika
    2 – Wyświetlenie wszystkich składników
    3 – Wyświetlenie składnika po nazwie (like)
    0 – Zakończenie programu
"""

import csv

read_file_ingredients = 'ingredients.csv'
output_file_ingridients = 'ingridients_dict_temp'

header = ["NAME", "CALORIES", "PROTEIN", "FAT", "CARBS", "FIBER", "TYPE"]
ingridients = []

with open(read_file_ingredients, encoding='utf-8', newline='') as data, \
     open(output_file_ingridients, 'w', encoding='utf-8') as output_file:

    print('import csv', file=output_file)
    print(file=output_file)

    reader = csv.DictReader(data)

    for row in reader:
        ingridients.append(row)

    print(']', file=output_file)



# Tworzenie klas i obiektów

class Ingridients:
    pass


print("Którą z czterech możliwości chcesz wybrać:\n"
      "1 – Dodanie nowego składnika \n"
      "2 – Wyświetlenie wszystkich składników \n"
      "3 – Wyświetlenie składnika po nazwie (like) \n"
      "0 – Zakończenie programu")
query = input("Podaj numerek: ")

