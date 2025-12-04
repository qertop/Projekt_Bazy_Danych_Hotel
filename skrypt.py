import pandas as pd

# Definicja danych dla wszystkich tabel
data = {
    "Kategoria": {
        "columns": ["ID_Kategorii", "Nazwa", "Cena_bazowa", "Opis"],
        "data": [[1, "Apartament Królewski", 450.00, "Widok na morze, jacuzzi"]]
    },
    "Pokoje": {
        "columns": ["ID_Pokoju", "Numer_pokoju", "Pietro", "ID_Kategorii", "Status"],
        "data": [[101, "205B", 2, 1, "Czysty"]]
    },
    "Sprzatanie": {
        "columns": ["ID_Sprzatania", "ID_Pokoju", "Data_sprzatania", "ID_Pracownika", "Status"],
        "data": [[505, 101, "2023-10-12 10:00", 5, "Wykonano"]]
    },
    "Restauracja": {
        "columns": ["ID_Restauracji", "ID_Pokoju", "Numer_stolika", "Kwota_zamowienia", "Data"],
        "data": [[77, 101, 12, 150.50, "2023-10-12 19:30"]]
    },
    "Basen": {
        "columns": ["ID_Basenu", "ID_Pokoju", "Liczba_osob", "Czas_pobytu_min", "Data_wejscia"],
        "data": [[33, 101, 2, 90, "2023-10-12 16:00"]]
    },
    "Parking": {
        "columns": ["ID_Parkingu", "ID_Pokoju", "Numer_miejsca", "Nr_rejestracyjny", "Koszt_doba"],
        "data": [[99, 101, "P-45", "WZ 12345", 50.00]]
    },
    "Gosc": {
        "columns": ["ID_Goscia", "Imie", "Nazwisko", "PESEL_Paszport", "Telefon"],
        "data": [[500, "Jan", "Kowalski", "90010112345", "+48 123 456 789"]]
    },
    "Rezerwacje": {
        "columns": ["ID_Rezerwacji", "ID_Goscia", "ID_Kategorii", "Data_od", "Data_do", "Status"],
        "data": [[20231001, 500, 1, "2023-12-24", "2023-12-27", "Potwierdzona"]]
    },
    "Przydzielenia": {
        "columns": ["ID_Przydzielenia", "ID_Rezerwacji", "ID_Pokoju", "ID_Goscia", "Data_przydzielenia"],
        "data": [[888, 20231001, 101, 500, "2023-12-24 14:00"]]
    },
    "Zameldowania": {
        "columns": ["ID_Zameldowania", "ID_Przydzielenia", "ID_Pracownika", "Data_zameldowania", "Uwagi"],
        "data": [[111, 888, 5, "2023-12-24 14:15", "Dostawka dla dziecka"]]
    },
    "Pracownik": {
        "columns": ["ID_Pracownika", "Imie", "Nazwisko", "Stanowisko", "Login"],
        "data": [[5, "Anna", "Nowak", "Recepcjonista", "a.nowak"]]
    },
    "Wymeldowania": {
        "columns": ["ID_Wymeldowania", "ID_Przydzielenia", "ID_Pracownika", "Data_wymeldowania", "Zwrot_klucza"],
        "data": [[222, 888, 5, "2023-12-27 11:00", "TAK"]]
    },
    "Platnosci_za_pobyt": {
        "columns": ["ID_Platnosci_Pobyt", "ID_Wymeldowania", "Kwota", "Waluta"],
        "data": [[701, 222, 1350.00, "PLN"]]
    },
    "Platnosci_do_rachunku": {
        "columns": ["ID_Platnosci_Rach", "ID_Wymeldowania", "Kwota", "Opis"],
        "data": [[702, 222, 200.00, "Minibar i Restauracja"]]
    },
    "Transakcje": {
        "columns": ["ID_Transakcji", "ID_Platnosci_Rach", "Usluga", "Kwota", "Data"],
        "data": [[901, 702, "Kolacja", 150.00, "2023-10-12"]]
    },
    "Dowod_zakupu": {
        "columns": ["ID_Dowodu", "ID_Transakcji", "Typ", "Numer", "Data_wystawienia"],
        "data": [[1001, 901, "Faktura", "FV/2023/12/99", "2023-12-27"]]
    }
}

# Tworzenie pliku Excel
output_file = 'struktura_bazy_hotelowej.xlsx'

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for sheet_name, content in data.items():
        df = pd.DataFrame(content["data"], columns=content["columns"])
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Plik '{output_file}' został wygenerowany pomyślnie! Każda tabela znajduje się w osobnej zakładce.")
