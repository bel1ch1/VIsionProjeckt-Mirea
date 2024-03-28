import streamlit as st
import hashlib
from DataBase import create_usertable, login_user


class Login:
    def login():
        user = st.sidebar.text_input('Username')
        passw = st.sidebar.text_input('Password',type='password')
        if st.sidebar.checkbox('Login') :
            create_usertable()
            hashed_pswd = make_hashes(passw)
            result = login_user(user,check_hashes(passw,hashed_pswd))
            if result:
                st.success("Logged In as {}".format(user))

                # Tasks For Only Logged In Users
                task = st.selectbox('Select Task',['Add Posts','Manage Blog','Profile'])
                if task == "Add Posts":
                    st.subheader("Add Articles")



def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False
