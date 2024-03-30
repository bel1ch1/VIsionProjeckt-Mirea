import streamlit as st
from DataBase.db_manager import register_user


# Форма регистрации
def register_form():
    st.subheader('Регистрация')
    new_username = st.text_input('Введите новое имя пользователя')
    new_password = st.text_input('Введите новый пароль', type='password')
    if st.button('Зарегистрировать'):
        register_user(new_username, new_password)
