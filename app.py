from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'
DATABASE = 'bank.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        
        conn = get_db()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists. Please choose a different one.', 'danger')
        finally:
            conn.close()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
        user = cursor.fetchone()
        conn.close()
        
        if user and check_password_hash(user[2], password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/admin')
def admin_panel():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('admin.html', username=session['username'])

@app.route('/user')
def user_panel():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('user.html', username=session['username'])

@app.route('/clients', methods=['GET'])
def get_clients():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Klienci")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

@app.route('/clients/<int:id>', methods=['GET'])
def get_client(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
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
            'phone': row[6],
            'balance': row[7]
        })
    else:
        return jsonify({'error': 'Client not found'}), 404

@app.route('/clients', methods=['POST'])
def add_client():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Klienci (name, surname, address, pesel, email, phone, balance) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (data['name'], data['surname'], data['address'], data['pesel'], data['email'], data['phone'], data['balance']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Client added'}), 201

@app.route('/clients/<int:id>', methods=['PUT'])
def update_client(id):
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Klienci SET name=?, surname=?, address=?, pesel=?, email=?, phone=?, balance=? WHERE id=?",
                   (data['name'], data['surname'], data['address'], data['pesel'], data['email'], data['phone'], data['balance'], id))
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