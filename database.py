import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('bank.db')
        self.cursor = self.conn.cursor()


    def create(self):
        "Function creates database Klienci-Transakcje-Konto"
        def create_table_clients(self):
            "Function creates table Klienci"
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS Klienci (
                                id INTEGER PRIMARY KEY,
                                imie VARCHAR(255),
                                nazwisko VARCHAR(255),
                                adres VARCHAR(255),
                                pesel VARCHAR(11),
                                email VARCHAR(255),
                                telefon VARCHAR(255)
                            )''')

        def create_table_accounts(self):
            "Function creates table Konta"
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS Konta (
                                id INTEGER PRIMARY KEY,
                                id_klienta INTEGER,
                                numer_rachunku VARCHAR(26),
                                saldo DECIMAL(10,2),
                                waluta VARCHAR(3),
                                typ_konta VARCHAR(255),
                                FOREIGN KEY (id_klienta) REFERENCES Klienci(id)
                            )''')

        def create_table_transactions(self):
            "Function creates table Transakcje"
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS Transakcje (
                                id INTEGER PRIMARY KEY,
                                id_konta INTEGER,
                                data DATETIME,
                                kwota DECIMAL(10,2),
                                waluta VARCHAR(3),
                                typ_transakcji VARCHAR(255),
                                opis VARCHAR(255),
                                FOREIGN KEY (id_konta) REFERENCES Konta(id)
                            )''')


    # Function adds Klient
    def add_client(self, imie, nazwisko, adres, pesel, email, telefon):
        self.cursor.execute('''INSERT INTO Klienci (imie, nazwisko, adres, pesel, email, telefon)
                          VALUES (?, ?, ?, ?, ?, ?)''', (imie, nazwisko, adres, pesel, email, telefon))

    # Function adds Konto
    def add_account(self, id_klienta, numer_rachunku, saldo, waluta, typ_konta):
        self.cursor.execute('''INSERT INTO Konta (id_klienta, numer_rachunku, saldo, waluta, typ_konta)
                          VALUES (?, ?, ?, ?, ?)''', (id_klienta, numer_rachunku, saldo, waluta, typ_konta))

    # Function adds Transakcja
    def add_transaction(self, id_konta, data, kwota, waluta, typ_transakcji, opis):
        self.cursor.execute('''INSERT INTO Transakcje (id_konta, data, kwota, waluta, typ_transakcji, opis)
                          VALUES (?, ?, ?, ?, ?, ?)''', (id_konta, data, kwota, waluta, typ_transakcji, opis))


    # Function removes Klient
    def usun_klienta(self, id_klienta):
        self.cursor.execute("DELETE FROM Klienci WHERE id=?", (id_klienta,))
        self.conn.commit()
        print("Klient o ID:", id_klienta, "został usunięty.")

    # Function removes Konto
    def usun_konto(self, id_konta):
        self.cursor.execute("DELETE FROM Konta WHERE id=?", (id_konta,))
        self.conn.commit()
        print("Konto o ID:", id_konta, "zostało usunięte.")

    # Function removes Transakcja
    def usun_transakcje(self, id_transakcji):
        self.cursor.execute("DELETE FROM Transakcje WHERE id=?", (id_transakcji,))
        self.conn.commit()
        print("Transakcja o ID:", id_transakcji, "została usunięta.")


    # Funkcja testowa wykonująca kilka operacji na bazie danych
    def add_test_records(self):
        # Połączenie z bazą danych
        self.create_table_clients()
        self.create_table_accounts()
        self.create_table_transactions()
        # Dodanie przykładowych danych
        self.add_client('Jan', 'Kowalski', 'ul. Testowa 123', '12345678901', 'jan@example.com', '123456789')
        self.add_client('Anna', 'Nowak', 'ul. Nowa 1', '98765432109', 'anna@example.com', '987654321')
        self.add_account(1, 'PL12345678901234567890123456', 1000.00, 'PLN', 'oszczędnościowe')
        self.add_account(2, 'PL98765432109876543210987654', 500.50, 'PLN', 'bieżące')
        self.add_transaction(1, '2024-02-25', 200.00, 'PLN', 'wpłata', 'Wpłata gotówki')

        # Zatwierdzenie zmian i zamknięcie połączenia
        self.conn.commit()

    def get_clients(self):
        self.cursor.execute("SELECT * FROM Klienci")
        rows = self.cursor.fetchall()
        return rows

    def get_accounts(self):
        self.cursor.execute("SELECT * FROM Konta")
        rows = self.cursor.fetchall()
        return rows

    def get_transactions(self):
        self.cursor.execute("SELECT * FROM Transakcje")
        rows = self.cursor.fetchall()
        return rows


    def display_clients(self):
        rows = self.get_clients()
        print("Clients:")
        #field_names = ["imie", "nazwisko", "adres", "PESEL", "email", "telefon"]
        for row in rows:
            print('| {:1} | {:^10} | {:^20} | {:^20} | {:^11} | {:^20} | {:^9}'.format(*row))

    def display_accounts(self):
        rows = self.get_accounts()
        print("Accounts:")
        for row in rows:
            print('| {:1} | {:^10} | {:^28} | {:^10} | {:^3} | {:^20} |'.format(*row))

    def display_transactions(self):
        rows = self.get_transactions()
        print("Accounts:")
        for row in rows:
            print('| {:1} | {:^1} | {:^10} | {:3} | {:^10} | {:^30} |'.format(*row))



if __name__ == "__main__":
    d = Database()
    d.display_clients()
    d.display_accounts()
    d.display_transactions()
