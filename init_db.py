import sqlite3
from flask import g
from config import Config

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(Config.DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Existing init_db function
def init_db():
    """Create the database schema."""
    conn = sqlite3.connect(Config.DATABASE)
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email EMAIL NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_link TEXT NOT NULL UNIQUE,
            userid INTEGER NOT NULL,
            FOREIGN KEY (userid) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

init_db()