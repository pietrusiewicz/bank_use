<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bank Application Documentation</title>
</head>
<body>
    <h1>Bank Application using Flask, Docker, SQL, Python</h1>
    <h2>Order of Implementation (To-Do List):</h2>
    <ol>
        <li>Python/SQL</li>
        <ul>
            <li>Designing tables</li>
            <li>Implementing demo console application</li>
            <li>Migrate to SQLAlchemy with Flask</li>
        </ul>
        <li>Flask</li>
        <ul>
            <li>Create a user-friendly website</li>
            <li>Migrate to SQLAlchemy with Flask</li>
        </ul>
        <li>Docker</li>
        <ul>
            <li>Containerize the application using Docker</li>
        </ul>
    </ol>
    <h2>1. Clients (Klienci):</h2>
    <ul>
        <li>id (int, primary key)</li>
        <li>name (varchar(255))</li>
        <li>surname (varchar(255))</li>
        <li>address (varchar(255))</li>
        <li>pesel (varchar(11))</li>
        <li>email (varchar(255))</li>
        <li>phone (varchar(255))</li>
    </ul>
    <h2>2. Accounts (Konta):</h2>
    <ul>
        <li>id (int, primary key)</li>
        <li>client_id (int, foreign key references Clients.id)</li>
        <li>account_number (varchar(26))</li>
        <li>balance (decimal(10,2))</li>
        <li>currency (varchar(3))</li>
        <li>account_type (varchar(255))</li>
    </ul>
    <h2>3. Transactions (Transakcje):</h2>
    <ul>
        <li>id (int, primary key)</li>
        <li>account_id (int, foreign key references Accounts.id)</li>
        <li>date (datetime)</li>
        <li>amount (decimal(10,2))</li>
        <li>currency (varchar(3))</li>
        <li>transaction_type (varchar(255))</li>
        <li>description (varchar(255))</li>
    </ul>
</body>
</html>