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
