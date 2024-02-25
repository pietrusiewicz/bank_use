Bank application what uses Flask what uses Docker, SQL, Python

1. Klienci:
id (int, primary key)
imię (varchar(255))
nazwisko (varchar(255))
adres (varchar(255))
pesel (varchar(11))
email (varchar(255))
telefon (varchar(255))
2. Konta:

id (int, primary key)
id_klienta (int, foreign key references Klienci.id)
numer_rachunku (varchar(26))
saldo (decimal(10,2))
waluta (varchar(3))
typ_konta (varchar(255))
3. Transakcje:

id (int, primary key)
id_konta (int, foreign key references Konta.id)
data (datetime)
kwota (decimal(10,2))
waluta (varchar(3))
typ_transakcji (varchar(255))
opis (varchar(255))
