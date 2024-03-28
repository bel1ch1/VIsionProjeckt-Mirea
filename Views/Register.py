import streamlit as st
import hashlib
from DataBase.db_manager import create_usertable, add_userdata


class Register:
    def reg_view():
        st.subheader("Create an Account")
        new_user = st.text_input('Username')
        new_passw = st.text_input('Password',type='password')
        if st.button('Sign Up'):
            create_usertable()
            add_userdata(new_user,make_hashes(new_passw))
            st.success("You have successfully created an account.Go to the Login Menu to login")


def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()



def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False
