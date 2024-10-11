from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash
from werkzeug.security import check_password_hash
from db_operations import DatabaseOperations

app = Flask(__name__)
app.secret_key = 'your_secret_key'

db_ops = DatabaseOperations()

@app.route('/')
def index():
    if 'username' in session:
        user_id = db_ops.get_user_id(session['username'])
        if user_id:
            return render_template('user.html', username=session['username'], user_id=user_id)
        else:
            flash('User not found.', 'danger')
            return redirect(url_for('logout'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        surname = request.form['surname']
        address = request.form['address']
        pesel = request.form['pesel']
        email = request.form['email']
        phone = request.form['phone']
        balance = request.form['balance']
        
        if db_ops.add_user(username, password):
            db_ops.add_client(name, surname, address, pesel, email, phone, balance)
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Username already exists. Please choose a different one.', 'danger')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = db_ops.get_db()
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

@app.route('/clients', methods=['GET'])
def get_clients():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    conn = db_ops.get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Klienci")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

@app.route('/clients/<int:id>', methods=['GET'])
def get_client(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    row = db_ops.get_client(id)
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
    db_ops.add_client(data['name'], data['surname'], data['address'], data['pesel'], data['email'], data['phone'], data['balance'])
    return jsonify({'status': 'Client added'}), 201

@app.route('/clients/<int:id>', methods=['PUT'])
def update_client(id):
    data = request.get_json()
    conn = db_ops.get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Klienci SET name=?, surname=?, address=?, pesel=?, email=?, phone=?, balance=? WHERE id=?",
                   (data['name'], data['surname'], data['address'], data['pesel'], data['email'], data['phone'], data['balance'], id))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Client updated'})

@app.route('/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    conn = db_ops.get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Klienci WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Client deleted'})

@app.route('/transfer', methods=['POST'])
def transfer_money():
    data = request.get_json()
    from_id = data['from_id']
    to_id = data['to_id']
    amount = data['amount']

    conn = db_ops.get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM Klienci WHERE id=?", (from_id,))
    from_balance = cursor.fetchone()
    if from_balance is None or from_balance[0] < amount:
        conn.close()
        return jsonify({'error': 'Insufficient funds or invalid sender ID'}), 400

    cursor.execute("SELECT balance FROM Klienci WHERE id=?", (to_id,))
    to_balance = cursor.fetchone()
    if to_balance is None:
        conn.close()
        return jsonify({'error': 'Invalid recipient ID'}), 400

    cursor.execute("UPDATE Klienci SET balance = balance - ? WHERE id=?", (amount, from_id))
    cursor.execute("UPDATE Klienci SET balance = balance + ? WHERE id=?", (amount, to_id))
    conn.commit()
    conn.close()

    return jsonify({'status': 'Transfer successful'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)