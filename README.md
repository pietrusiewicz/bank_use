<h1>Bank application what uses Flask what uses Docker, SQL, Python</h1>
Order implementation (todolist):
<ol>
  <li>python/sql</li>
  <ul>
    <li>englishing tables</li>
    <li>implementing demo console application</li>
    <li>migrate to sqlalchemy while flask</li>
  </ul>
  <li>flask</li>
  <ul>
    <li>migrate to sqlalchemy while flask</li>
  </ul>
  <li>docker</li>
  <ul>
    <li>move to docker</li>
  </ul>
</ol>
<h2>1. Klienci:</h2>
<ul>
  <li>id (int, primary key)</li>
  <li>imię (varchar(255))</li>
  <li>nazwisko (varchar(255))</li>
  <li>adres (varchar(255))</li>
  <li>pesel (varchar(11))</li>
  <li>email (varchar(255))</li>
  <li>telefon (varchar(255))</li>
</ul>
<br/>
<h2>2. Konta:</h2>
<ul>
  <li>id (int, primary key)</li>
  <li>id_klienta (int, foreign key references Klienci.id)</li>
  <li>numer_rachunku (varchar(26))</li>
  <li>saldo (decimal(10,2))</li>
  <li>waluta (varchar(3))</li>
  <li>typ_konta (varchar(255))</li>
</ul>
<h2>3. Transakcje:</h2>
<ul>
  <li>id (int, primary key)</li>
  <li>id_konta (int, foreign key references Konta.id)</li>
  <li>data (datetime)</li>
  <li>kwota (decimal(10,2))</li>
  <li>waluta (varchar(3))</li>
  <li>typ_transakcji (varchar(255))</li>
  <li>opis (varchar(255))</li>
</ul>
