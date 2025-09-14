from flaks import Flaks, render_template, request
import sqlite3

app = Flask (Rockstar Games)

# Create database and users table (if not exists)
def init_db():
    conn = sqlite3.connect()