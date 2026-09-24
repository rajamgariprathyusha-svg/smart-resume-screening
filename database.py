import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


# -----------------------------------
# Create Users Table
# -----------------------------------
def create_table():

    conn = sqlite3.connect("users.db", timeout=10)

    try:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT UNIQUE,
            password TEXT
        )
        """)

        conn.commit()

    finally:
        conn.close()


# -----------------------------------
# Register User
# -----------------------------------
def register_user(username, email, password):

    conn = sqlite3.connect("users.db", timeout=10)

    try:
        cursor = conn.cursor()

        # Convert password into secure hash
        hashed_password = generate_password_hash(password)

        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, hashed_password)
        )

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


# -----------------------------------
# Login User
# -----------------------------------
def login_user(email, password):

    conn = sqlite3.connect("users.db", timeout=10)

    try:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        )

        user = cursor.fetchone()

    finally:
        conn.close()

    if user:

        # Check entered password against stored hash
        if check_password_hash(user[3], password):
            return user

    return None


# -----------------------------------
# Check Email
# -----------------------------------
def check_email(email):

    conn = sqlite3.connect("users.db", timeout=10)

    try:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        )

        user = cursor.fetchone()

    finally:
        conn.close()

    return user


# -----------------------------------
# Update Password
# -----------------------------------
def update_password(email, new_password):

    conn = sqlite3.connect("users.db", timeout=10)

    try:
        cursor = conn.cursor()

        # Hash the new password before saving
        hashed_password = generate_password_hash(new_password)

        cursor.execute(
            "UPDATE users SET password = ? WHERE email = ?",
            (hashed_password, email)
        )

        conn.commit()
        return True

    finally:
        conn.close()

