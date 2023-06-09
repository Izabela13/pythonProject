import csv

medals_table = [
	{'athlete': 'CASLAVSKA, Vera', 'gold': 7, 'silver': 4, 'bronze': 0, 'country': 'Czechoslovakia', 'total': None},
	{'athlete': 'FISCHER, Birgit', 'gold': 8, 'silver': 4, 'bronze': 0, 'country': 'East Germany', 'total': None},
	{'athlete': 'NURMI, Paavo', 'gold': 9, 'silver': 3, 'bronze': 0, 'country': 'Finland', 'total': None},
	{'athlete': 'VAN ALMSICK, Franziska', 'gold': 0, 'silver': 4, 'bronze': 6, 'country': 'Germany', 'total': None},
	{'athlete': 'GEREVICH, Aladar', 'gold': 7, 'silver': 1, 'bronze': 2, 'country': 'Hungary', 'total': None},
	{'athlete': 'KELETI, Agnes', 'gold': 5, 'silver': 3, 'bronze': 2, 'country': 'Hungary', 'total': None},
	{'athlete': 'MANGIAROTTI, Edoardo', 'gold': 6, 'silver': 5, 'bronze': 2, 'country': 'Italy', 'total': None},
	{'athlete': 'GAUDINI, Giulio', 'gold': 3, 'silver': 4, 'bronze': 2, 'country': 'Italy', 'total': None},
	{'athlete': 'ONO, Takashi', 'gold': 5, 'silver': 4, 'bronze': 4, 'country': 'Japan', 'total': None},
	{'athlete': 'KATO, Sawao', 'gold': 8, 'silver': 3, 'bronze': 1, 'country': 'Japan', 'total': None},
	{'athlete': 'NAKAYAMA, Akinori', 'gold': 6, 'silver': 2, 'bronze': 2, 'country': 'Japan', 'total': None},
	{'athlete': 'COMANECI, Nadia', 'gold': 5, 'silver': 3, 'bronze': 1, 'country': 'Romania', 'total': None},
	{'athlete': 'NEMOV, Alexei', 'gold': 4, 'silver': 2, 'bronze': 6, 'country': 'Russia', 'total': None},
	{'athlete': 'LATYNINA, Larisa', 'gold': 9, 'silver': 5, 'bronze': 4, 'country': 'Soviet Union', 'total': None},
	{'athlete': 'ANDRIANOV, Nikolay', 'gold': 7, 'silver': 5, 'bronze': 3, 'country': 'Soviet Union', 'total': None},
	{'athlete': 'SHAKHLIN, Boris', 'gold': 7, 'silver': 4, 'bronze': 2, 'country': 'Soviet Union', 'total': None},
	{'athlete': 'CHUKARIN, Viktor Ivanovich', 'gold': 7, 'silver': 3, 'bronze': 1, 'country': 'Soviet Union', 'total': None},
	{'athlete': 'ASTAKHOVA, Polina', 'gold': 5, 'silver': 2, 'bronze': 3, 'country': 'Soviet Union', 'total': None},
	{'athlete': 'DITYATIN, Aleksandr', 'gold': 3, 'silver': 6, 'bronze': 1, 'country': 'Soviet Union', 'total': None},
	{'athlete': 'SCHERBO, Vitaly', 'gold': 6, 'silver': 0, 'bronze': 4, 'country': 'Unified team', 'total': None},
	{'athlete': 'PHELPS, Michael', 'gold': 14, 'silver': 0, 'bronze': 2, 'country': 'United States', 'total': None},
	{'athlete': 'THOMPSON, Jenny', 'gold': 8, 'silver': 3, 'bronze': 1, 'country': 'United States', 'total': None},
	{'athlete': 'TORRES, Dara', 'gold': 4, 'silver': 4, 'bronze': 4, 'country': 'United States', 'total': None},
	{'athlete': 'BIONDI, Matthew', 'gold': 8, 'silver': 2, 'bronze': 1, 'country': 'United States', 'total': None},
	{'athlete': 'COUGHLIN, Natalie', 'gold': 3, 'silver': 4, 'bronze': 4, 'country': 'United States', 'total': None},
	{'athlete': 'OSBURN, Carl Townsend', 'gold': 5, 'silver': 4, 'bronze': 2, 'country': 'United States', 'total': None},
	{'athlete': 'SPITZ, Mark', 'gold': 9, 'silver': 1, 'bronze': 1, 'country': 'United States', 'total': None},
	{'athlete': 'HALL, Gary Jr.', 'gold': 5, 'silver': 3, 'bronze': 2, 'country': 'United States', 'total': None},
	{'athlete': 'LEWIS, Carl', 'gold': 9, 'silver': 1, 'bronze': 0, 'country': 'United States', 'total': None},
]

column_names = ['athlete', 'gold', 'silver', 'bronze', 'country', 'total']

filename = 'athlete_medal_write.csv'

with open(filename, 'w', encoding='utf-8', newline='') as output_file:
	# Tworzenie obiektu writer. Do DictWritera trzeba podać, jaki jest plik wyjściowy
	writer = csv.DictWriter(output_file, fieldnames=column_names, quoting=csv.QUOTE_NONNUMERIC)
	writer.writeheader()  # metoda, do której nie trzeba teraz nic przekazywać.
	writer.writerows(medals_table)  # chcemy tu przekazać całą tabelę 'medals_table'

"""
Analiza: 

Tworząc nasz obiekt DICTWRITERA podaliśmy mu, że nazwy naszych kolumn 'fieldnames=column_names'.
Czyli podaliśmy mu, że to są nazwy kolumn, które zdefiniowaliśmy dla zmiennej 'column_names': 
	column_names = ['athlete', 'gold', 'silver', 'bronze', 'country', 'total']
Obiekt DictWriter wie, po jakich nazwach w mapach szukać sobie danych (jest to dla niego hint - wskazówka). 

Następnie wywołaliśmy na obiekcie DictWriter metodę WRITEHEADER().
Do tej metody nie przekazaliśmy nic. 
	writer.writeheader()
Nie przekazaliśmy do niej nic dlatego, że DictWriter już wie, jakie ma nazwy headerów, ponieważ ma podane: 
	fieldnames=column_names.
DictWriter wie, że są to kolejno: 'athlete', 'gold', 'silver', 'bronze', 'country', 'total'. 
Dla DictWritera nagłówki kolumn są oczywiste, ponieważ zostały przekazane wcześniej. Dlatego do metody 'writeheader()'
nie zostało podane nic. 

Na samym końcu przekazaliśmy do metody WRITEROWS() całą listę z naszymi mapami, czyli 'medals_table': 
	writer.writerows(medals_table)
Mając dane o headerach i o liście DictWriter zaczyna po niej przechodzić (iterować). DictWriter sprawdza, jakie nazwy
kolumn zostały mu przekazane (jako nazwa klucza) i na tej podstawie wyciąga dane (wartości przypisane dla kluczy). 

DictWriter przekonwertował plik pythonowy na plik csv rozdzielony przecinkami.
"""


"""
Można podejść inaczej i zamiast metody writerows() zastosować iterację po każdym wierszu (mapie/ słowniku). 
"""

with open(filename, 'w', encoding='utf-8', newline='') as output_file:
	writer = csv.DictWriter(output_file, fieldnames=column_names, quoting=csv.QUOTE_NONNUMERIC)
	writer.writeheader()

	for row in medals_table:
		writer.writerow(row)

"""
W drugim podejściu iterujemy po całej tablicy i wstawiamy wiersz po wierszu. 
To podejście jest przydante, jeśli chcemy dokonać jakiejś manipulacji na danych, np. sortowanie.
"""


def sort_key(d: dict) -> str:
	return d['athlete']


with open(filename, 'w', encoding='utf-8', newline='') as output_file:
	writer = csv.DictWriter(output_file, fieldnames=column_names, quoting=csv.QUOTE_NONNUMERIC)
	writer.writeheader()
	writer.writerows(sorted(medals_table, key=sort_key))  # przekazujemy tutaj medal_tables, ale od razu sortujemy
	"""
	Uwaga, mamy słownik. Nie można zastosować metody 'sorted()' dla słownika. DictWriter nie może porównać słowników
	między sobą. 
	
		writer.writerows(sorted(medals_table))
	
	Można natomiast wprowadzić jakąś funkcję sortującą.
	Nasza funkcja musi przyjąć jakiś argument. Naszymi danymi w naszej tabeli są słowniki. 
	Nasza funkcja będzie przyjmować argument 'd' od 'dictionary'. 
	
		def sorted(d: dict) -> str: 
			return d['athlete']
	
	Dokonujemy od razu typowania. 'dict' będzie zamieniany na 'str'. Nasza funkcja ma zwracać stringi, ponieważ chcemy
	posortować dane po nazwiskach. Jedyne, co musimy zrobić, to zwrócić odpowiednią daną. W tym wypadku będzie to atleta.
	
	Do zmiennej możemy przypisać funkcję i ze zmiennej ją wywołać. Tak więc w metodzie sorted() przekazujemy dodatkowy
	parametr 'key'. Parametr 'key' oczekuje, aby przekazać mu jakąś funkcję. 
	
	Intelisense od razu zawinie funkcję w nawiasy. My przekazujemy tylko nazwę funkcji. Trzeba pamiętać o usunięciu 
	nawiasów. 
	
	Przez naszą funkcję przekazujemy informację: posortuj naszą tabelę 'medal_tables' według wskazanego klucza.
	Interpreter patrzy na wskazany klucz. W tym przypadku 'athlete'. Po tym kluczu dokona sortowania.
	"""