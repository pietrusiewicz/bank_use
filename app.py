from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
DATABASE = 'bank.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clients', methods=['GET'])
def get_clients():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Klienci")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

@app.route('/clients/<int:id>', methods=['GET'])
def get_client(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Klienci WHERE id=?", (id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return jsonify({
            'id': row[0],
            'name': row[1],
            'surname': row[2],
            'address': row[3],
            'pesel': row[4],
            'email': row[5],
            'phone': row[6]
        })
    else:
        return jsonify({'error': 'Client not found'}), 404

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

@app.route('/clients/<int:id>', methods=['PUT'])
def update_client(id):
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Klienci SET name=?, surname=?, address=?, pesel=?, email=?, phone=? WHERE id=?",
                   (data['name'], data['surname'], data['address'], data['pesel'], data['email'], data['phone'], id))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Client updated'})

@app.route('/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Klienci WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Client deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)