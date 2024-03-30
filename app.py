# Рисуем сайт подставляя формы из streamlit_scripts

# Импортируем
import streamlit as st
from streamlit_scripts.Login import login_form
from streamlit_scripts.Register import register_form
from streamlit_scripts.ViewDetector import view_detector


with st.sidebar:
    # Форма для регистрации нового пользователя
    register_form()
    # Форма для аутентификации пользователя
    login_form()

if st.session_state.log_in:
    st.session_state['view'] = True
    if st.session_state.view == True:
        view_detector()
    del st.session_state.view
