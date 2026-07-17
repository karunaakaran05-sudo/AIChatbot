import streamlit as st

from pages.home import home_page
from pages.login import login_page
from pages.register import register_page
from pages.chat import chat_page
from pages.history import history_page
from pages.profile import profile_page

from auth.session import initialize_session


st.set_page_config(
    page_title="AI Customer Support",
    page_icon="🤖",
    layout="wide"
)

initialize_session()

if st.session_state.logged_in:

    menu = {
        "🏠 Home": home_page,
        "💬 Chat": chat_page,
        "📜 History": history_page,
        "👤 Profile": profile_page,
    }

else:

    menu = {
        "🏠 Home": home_page,
        "🔐 Login": login_page,
        "📝 Register": register_page,
    }

choice = st.sidebar.selectbox(
    "Navigation",
    list(menu.keys())
)

menu[choice]()
if choice == "Home":
    home_page()

elif choice == "Login":
    login_page()

elif choice == "Register":
    register_page()

elif choice == "Chat":
    chat_page()

elif choice == "History":
    history_page()

elif choice == "Profile":
    profile_page()