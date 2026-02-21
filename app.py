from flask import Flask, request, render_template, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import logging

app = Flask(__name__)

logging.basicConfig(filename='audit.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def init_db():
    conn = sqlite3.connect('users.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
    conn.close()

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('users.db')
    cursor = conn.execute('SELECT password FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    
    if user and check_password_hash(user[0], password):
        logging.info(f"SUCCESSFUL LOGIN: User {username}")
        return "Access Granted"
    else:
        logging.warning(f"FAILED LOGIN ATTEMPT: User {username}")
        return "Access Denied", 401

if __name__ == '__main__':
    init_db()
    app.run(debug=False) 
