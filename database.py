import sqlite3

# Funkcja tworząca tabeli Klienci
def create_table_clients(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS Klienci (
                        id INTEGER PRIMARY KEY,
                        imie VARCHAR(255),
                        nazwisko VARCHAR(255),
                        adres VARCHAR(255),
                        pesel VARCHAR(11),
                        email VARCHAR(255),
                        telefon VARCHAR(255)
                    )''')

# Funkcja tworząca tabeli Konta
def create_table_accounts(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS Konta (
                        id INTEGER PRIMARY KEY,
                        id_klienta INTEGER,
                        numer_rachunku VARCHAR(26),
                        saldo DECIMAL(10,2),
                        waluta VARCHAR(3),
                        typ_konta VARCHAR(255),
                        FOREIGN KEY (id_klienta) REFERENCES Klienci(id)
                    )''')

# Funkcja tworząca tabeli Transakcje
def create_table_transactions(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS Transakcje (
                        id INTEGER PRIMARY KEY,
                        id_konta INTEGER,
                        data DATETIME,
                        kwota DECIMAL(10,2),
                        waluta VARCHAR(3),
                        typ_transakcji VARCHAR(255),
                        opis VARCHAR(255),
                        FOREIGN KEY (id_konta) REFERENCES Konta(id)
                    )''')

# Funkcja dodająca klienta
def add_client(cursor, imie, nazwisko, adres, pesel, email, telefon):
    cursor.execute('''INSERT INTO Klienci (imie, nazwisko, adres, pesel, email, telefon)
                      VALUES (?, ?, ?, ?, ?, ?)''', (imie, nazwisko, adres, pesel, email, telefon))

# Funkcja dodająca konto
def add_account(cursor, id_klienta, numer_rachunku, saldo, waluta, typ_konta):
    cursor.execute('''INSERT INTO Konta (id_klienta, numer_rachunku, saldo, waluta, typ_konta)
                      VALUES (?, ?, ?, ?, ?)''', (id_klienta, numer_rachunku, saldo, waluta, typ_konta))

# Funkcja dodająca transakcję
def add_transaction(cursor, id_konta, data, kwota, waluta, typ_transakcji, opis):
    cursor.execute('''INSERT INTO Transakcje (id_konta, data, kwota, waluta, typ_transakcji, opis)
                      VALUES (?, ?, ?, ?, ?, ?)''', (id_konta, data, kwota, waluta, typ_transakcji, opis))

# Funkcja do usuwania klienta
def usun_klienta(id_klienta):
    conn = sqlite3.connect('moja_baza.db')
    c = conn.cursor()
    c.execute("DELETE FROM Klienci WHERE id=?", (id_klienta,))
    conn.commit()
    print("Klient o ID:", id_klienta, "został usunięty.")
    conn.close()

# Funkcja do usuwania konta
def usun_konto(id_konta):
    conn = sqlite3.connect('moja_baza.db')
    c = conn.cursor()
    c.execute("DELETE FROM Konta WHERE id=?", (id_konta,))
    conn.commit()
    print("Konto o ID:", id_konta, "zostało usunięte.")
    conn.close()

# Funkcja do usuwania transakcji
def usun_transakcje(id_transakcji):
    conn = sqlite3.connect('moja_baza.db')
    c = conn.cursor()
    c.execute("DELETE FROM Transakcje WHERE id=?", (id_transakcji,))
    conn.commit()
    print("Transakcja o ID:", id_transakcji, "została usunięta.")
    conn.close()


# Funkcja testowa wykonująca kilka operacji na bazie danych
def add_test_records():
    # Połączenie z bazą danych
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    # Utworzenie tabel, jeśli nie istnieją
    create_table_clients(cursor)
    create_table_accounts(cursor)
    create_table_transactions(cursor)

    # Dodanie przykładowych danych
    add_client(cursor, 'Jan', 'Kowalski', 'ul. Testowa 123', '12345678901', 'jan@example.com', '123456789')
    add_client(cursor, 'Anna', 'Nowak', 'ul. Nowa 1', '98765432109', 'anna@example.com', '987654321')
    add_account(cursor, 1, 'PL12345678901234567890123456', 1000.00, 'PLN', 'oszczędnościowe')
    add_account(cursor, 2, 'PL98765432109876543210987654', 500.50, 'PLN', 'bieżące')
    add_transaction(cursor, 1, '2024-02-25', 200.00, 'PLN', 'wpłata', 'Wpłata gotówki')

    # Zatwierdzenie zmian i zamknięcie połączenia
    conn.commit()
    conn.close()

def wyswietl_klientow():
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Klienci")
    rows = c.fetchall()
    print("Klienci:")
    for row in rows:
        print(row)
    conn.close()

# Funkcja do wyświetlania kont
def wyswietl_konta():
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Konta")
    rows = c.fetchall()
    print("Konta:")
    for row in rows:
        print(row)
    conn.close()

# Funkcja do wyświetlania transakcji
def wyswietl_transakcje():
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Transakcje")
    rows = c.fetchall()
    print("Transakcje:")
    for row in rows:
        print(row)
    conn.close()

if __name__ == "__main__":
    add_test_records()
    wyswietl_klientow()
    wyswietl_konta()
    wyswietl_transakcje()
