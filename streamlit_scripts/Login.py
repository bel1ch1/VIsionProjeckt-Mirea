import streamlit as st
from DataBase.db_manager import login_user


# Форма для логина
def login_form():
    st.subheader('Вход')
    login_username = st.text_input('Введите имя пользователя',)
    login_password = st.text_input('Введите пароль', type='password')
    if st.button('Войти', key='log_in'):
        login_user(login_username, login_password)

# def add_session():
#     if 'btn_log' not in st.session_state:
#         st.session_state.btn_log = True
