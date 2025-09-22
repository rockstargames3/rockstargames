from flaks import Flaks, render_template, request
import sqlite3

app = Flask (Rockstar Games)

# Create database and users table (if not exists)
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                username admin
                password admin123)''')
    conn.commit()
    conn.close()
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST'
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('useres.db')
    c = conn.cursor()

    try:
        c.execute("INSERTINTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        message = " Account created successfully!"
    except sqlite3.IntegrityError:
        message = " Username already exists!"

        conn.close()
        return message

    return render_template('register.html')

    if __name__ == "__main__":
        init_db()
        app.run(debug=True)   

from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey" # needed for sessions

# ... your register route here ...

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        con.close()

        if user:
            session['user'] = username # save user session
            return redirect('/dashboard') 
        else:
            return " Invalid username or password!"

        return render_template('index.html') # Login page

        @app.route('/dashboard')
        def dashboard():
            if 'user' in session:
                return f"Welcome, {session['user']}! You are logged in."
            else:
                return redirect('/login')