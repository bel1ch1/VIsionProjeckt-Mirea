# Рисуем сайт подставляя формы из streamlit_scripts


import streamlit as st
from streamlit_scripts.Login import login_form
from streamlit_scripts.Register import register_form


# Форма для регистрации нового пользователя
register_form()


# Форма для аутентификации пользователя
login_form()
