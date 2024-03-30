import streamlit as st


# Форма регистрации
st.subheader('Регистрация')
new_username = st.text_input('Введите новое имя пользователя')
new_password = st.text_input('Введите новый пароль', type='password')
