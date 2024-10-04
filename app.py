from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'bank.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/clients', methods=['GET'])
def get_clients():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Klienci")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

@app.route('/clients', methods=['POST'])
def add_client():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Klienci (name, surname, address, pesel, email, phone) VALUES (?, ?, ?, ?, ?, ?)",
                   (data['name'], data['surname'], data['address'], data['pesel'], data['email'], data['phone']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Client added'}), 201

@app.route('/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Klienci WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Client deleted'})

# Similar routes for accounts and transactions can be added here

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)