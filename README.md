# Bank Application

This is a simple bank application built using Flask, Docker, and SQLite. The application allows you to manage clients, accounts, and transactions.

## Prerequisites

- Docker
- Docker Compose
- Python 3.9 (for initializing the database)

## Setup

### 1. Clone the Repository

```sh
git clone https://github.com/pietrusiewicz/bank_use.git
cd bank_use
```
### 2. Initialize the Database

Before running the application, initialize the SQLite database:

```sh 
python init_db.py
```

### 3. Build and Run the Docker Containers

Use Docker Compose to build and run the containers:
```sh
docker-compose up --build
```

This command will build the Docker image and start the Flask application. The application will be accessible at http://localhost:5000.

### 4. Usage
### Warning!
To use **curl** command you have to enter container' cli:
```sh
docker exec -it <container_id> /bin/bash
```
<sup>
<b>container_id</b> is contained in command <u><i>docker ps</i></u>
</sup>

#### Get All Clients
<ul>
  <li>URL: /clients</li>
  <li>Method: GET</li>
  <li>Description: Retrieves a list of all clients.</li>
</ul>

```sh
curl -X GET http://localhost:5000/clients
```

#### Add a New Client
URL: /clients
Method: POST
Description: Adds a new client.
Request with JSON:
```sh
curl -X POST http://localhost:5000/clients -H "Content-Type: application/json" -d '{
  "name": "John",
  "surname": "Doe",
  "address": "123 Main St",
  "pesel": "12345678901",
  "email": "john.doe@example.com",
  "phone": "123-456-7890"
}'
```

#### Delete a Client
URL: /clients/<id>
Method: DELETE
Description: Deletes a client by ID.
```sh
curl -X DELETE http://localhost:5000/clients/1
```

#### Stopping the Application
To stop the application, press Ctrl+C in the terminal where docker-compose up is running, or run:
```sh
docker-compose down
```
This will stop and remove the containers.
