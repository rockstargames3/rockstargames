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