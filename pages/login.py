import streamlit as st

from database.database import SessionLocal
from auth.auth_service import login_user
from auth.session import login_user as create_session


def login_page():

    st.title("🔐 Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        # Input validation
        if not email or not password:
            st.warning("Please enter both email and password.")
            return

        db = SessionLocal()

        try:
            success, message, user = login_user(
                db,
                email,
                password
            )

            if success:
                create_session(user)
                st.success(message)
                st.rerun()

            else:
                st.error(message)

        except Exception as e:
            st.error(f"Login Error: {e}")

        finally:
            db.close()