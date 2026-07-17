import streamlit as st


def initialize_session():
    """
    Initialize session state variables.
    """

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "user_id" not in st.session_state:
        st.session_state.user_id = None

    if "user_name" not in st.session_state:
        st.session_state.user_name = ""

    if "user_email" not in st.session_state:
        st.session_state.user_email = ""


def login_user(user):
    """
    Store user information after successful login.
    """

    st.session_state.logged_in = True
    st.session_state.user_id = user.id
    st.session_state.user_name = user.full_name
    st.session_state.user_email = user.email


def logout_user():
    """
    Clear session after logout.
    """

    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.user_name = ""
    st.session_state.user_email = ""


def is_logged_in():
    """
    Return login status.
    """

    return st.session_state.logged_in