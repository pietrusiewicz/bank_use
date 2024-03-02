from database import Database

class App:
    def __init__(self):
        self.d = Database()
        self.menu()


    def menu(self):
        """
        Primitive demo database play:
            select table:
            1) Klienci
            2) Konta
            3) Transakcje
        After select displays database with hotkeys to operate
        """
        while True:
            select = input("""select table:
                1) Klienci
                2) Konta
                3) Transakcje
            """)
            
            if select == '1':
                self.manage_clients()

            if select == '2':
                self.manage_accounts()

            if select == '3':
                self.manage_transactions()

    def manage_clients(self):
        while True:
            self.d.display_clients()
            select = input("""a-ADD u-UPDATE d-DELETE
            """).lower()
            if select == 'a':
                imie,nazwisko,adres,pesel,email,numer=[input("imie: "),input("nazwisko: "),input("adres: "),input("pesel: "),input("email: "),input("nr telefonu: ")]

                self.d.add_client(imie,nazwisko,adres,pesel,email,numer)

            if select == 'u':
                fields = ["imie","nazwisko","adres","pesel","email","numer telefonu"]
                i = int(input("UPDATE)\npodaj id\n"))
                field = fields[int(input(f"Podaj pole:\n{list(enumerate(fields))}"))]
                value = input("podaj wartosc\n")

                self.d.update_client(field,value,i)

            if select == 'd':
                i = input("podaj id\n")
                self.d.usun_klienta(i)

    def manage_accounts(self):
        while True:
            self.d.display_accounts()
            select = input("""a-ADD u-UPDATE d-DELETE
            """).lower()

            if select == 'a':
                id_klienta,nr_rachunku,saldo,waluta,typ_konta = [input("id_klienta: "),input("numer_rachunku: "),input("saldo: "),input("waluta: "),input("typ konta: ")]

                self.d.add_account(id_klienta,nr_rachunku,saldo,waluta,typ_konta)

            if select == 'u':
                fields = ["id_klienta","nr_rachunku","saldo","waluta","typ_konta"]
                i = int(input("UPDATE)\npodaj id\n"))
                field = fields[int(input(f"Podaj pole:\n{list(enumerate(fields))}"))]
                value = input("podaj wartosc\n")

                self.d.update_account(field,value,i)

            if select == 'd':
                i = input("podaj id\n")
                self.d.usun_konto(i)

    def manage_transactions(self):
        while True:
            self.d.display_transactions()
            select = input("""a-ADD u-UPDATE d-DELETE
            """)

if __name__ == '__main__':
    a = App()
