import streamlit as st


# Форма для логина
st.subheader('Вход')
login_username = st.text_input('Введите имя пользователя')
login_password = st.text_input('Введите пароль', type='password')
