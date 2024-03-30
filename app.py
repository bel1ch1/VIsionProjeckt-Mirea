import streamlit as st
import os
from DataBase.db_manager import register_user, login_user

# Рисуем

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
