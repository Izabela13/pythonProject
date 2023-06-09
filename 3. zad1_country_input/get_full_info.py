"""
Polecenie: Napisz program, gdzie po wpisaniu w konsoli nazwy kraju, niezależnie od wielkości znaków, albo kodu krótkiego
(CC), wyprintowały się informacje o stolicy, strefie czasowej, walucie.
"""

filename = 'country_info.txt'
countries_dict = {}  # mapa (słownik) krajów. Inicjacja nowej mapy krajów.

with open(filename, encoding='utf-8') as country_file:
    for line in country_file:
        data = line.strip().split('|')
        country, capital, cc, cc3, iac, timezone, currency = data  # tablica/ lista rozpakowana
        # po kolei wymieniane są nazwy zmiennych, które składają się na tablicę/ listę ("data").

        # Zasilanie mapy (słownika) "countries_dict"
        countries_dict[country.casefold()] = data
        """do mapy 'countries' chcemy włożyć po takim kluczu jak 'country' zapisać tabele 
           metoda casefold() tworzy małe litery - spowoduje, że wielkość liter nie będzie miała znaczenia """
        countries_dict[cc.casefold()] = data

        """ Mapa, którą wstawimy w miejsce 'VALUE'. Kluczem będzie kraj, a wartością będzie kolejna mapa. """
        # Tworzenie mapy z danymi
        country_info_map = {
            'capital': capital,
            'timezone': timezone,
            'iac': iac,
            'currency': currency
        }

        # Zasilanie mapy (słownika) "countries_dict"
        """ Mapa krajów podstawiana jest w miejsce tabeli pod klucze kraju i kodu kraju. 
            Mamy przygotowaną strukturę, z której będziemy wyciągać dane. """
        countries_dict[country.casefold()] = country_info_map
        countries_dict[cc.casefold()] = country_info_map


while True:
    selected_country = input("Podaj kraj lub kod: ")
    if selected_country == "":  # defensywne programowanie - jeżeli nic nie zostanie podane, wyjdź z pętli
        break  # można jeszcze zapisać 'if not selected_country'. Po tym też nastąpi 'break'

    result = countries_dict.get(selected_country.casefold())  # dostawanie się w sposób bezpieczny do danych - metoda get()
    if result:  # jeśli klucz istnieje, chcemy wyprintować dane
        print(f"Stolica: {result['capital']}",
              f"Strefa czasowa: {result['timezone']}"
              f"Kod kierunkowy: {result['iac']}",
              f"Waluta: {result['currency']}",
              sep='\n\t')
        print("")
    else:
        print(f"Nie ma takiego klucza jak {selected_country} \n")

"""
f - od 'format. Jeśli postawimy 'f' przed stringiem i w curly bracets {} wstawiamy tekst, to automatycznie 
ten tekst jest podstawiany.
"""