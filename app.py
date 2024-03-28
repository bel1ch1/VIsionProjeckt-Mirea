import streamlit as st
import sqlite3
from passlib.hash import pbkdf2_sha256
import os

# Создаем соединение с базой данных (или открываем существующую базу данных)
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Создаем таблицу пользователей (если она еще не существует)
c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')

# Функция для регистрации нового пользователя
def register_user(username, password):
    hashed_password = pbkdf2_sha256.hash(password)
    c.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, hashed_password))
    conn.commit()
    st.success("Пользователь зарегистрирован")

# Функция для аутентификации пользователя
def login_user(username, password):
    c.execute('''SELECT password FROM users WHERE username = ?''', (username,))
    result = c.fetchone()
    if result and pbkdf2_sha256.verify(password, result[0]):
        st.success("Успешная аутентификация")
    else:
        st.warning("Неверное имя пользователя или пароль")


# Форма для регистрации нового пользователя
st.subheader('Регистрация')
new_username = st.text_input('Введите новое имя пользователя')
new_password = st.text_input('Введите новый пароль', type='password')
if st.button('Зарегистрировать'):
    register_user(new_username, new_password)

# Форма для аутентификации пользователя
st.subheader('Вход')
login_username = st.text_input('Введите имя пользователя')
login_password = st.text_input('Введите пароль', type='password')
if st.button('Войти'):
    login_user(login_username, login_password)
