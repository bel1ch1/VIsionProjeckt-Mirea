import sqlite3
import streamlit as st
from passlib.hash import pbkdf2_sha256

# Подключение
conn = sqlite3.connect('data.db', check_same_thread=False)
cur = conn.cursor()


# Создаем таблицу пользователей (если она еще не существует)
cur.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')


# Функция для регистрации нового пользователя
def register_user(username, password):
    hashed_password = pbkdf2_sha256.hash(password)
    cur.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, hashed_password))
    conn.commit()
    st.success("Пользователь зарегистрирован")


# Функция для аутентификации пользователя
def login_user(username, password):
    cur.execute('''SELECT password FROM users WHERE username = ?''', (username,))
    result = cur.fetchone()
    if result and pbkdf2_sha256.verify(password, result[0]):
        st.success("Успешная аутентификация")
    else:
        st.warning("Неверное имя пользователя или пароль")
