import os
import pickle
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Hardcoded credentials (sensitive information exposure)
DB_USER = "admin"
DB_PASS = "password123"
DB_NAME = "users.db"


@app.route("/login", methods=["GET"])
def login():
    # SQL Injection vulnerability
    username = request.args.get("username")
    password = request.args.get("password")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # ⚠️ Vulnerable: direct string concatenation (SQL injection)
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        return f"
