import streamlit as st

from auth.session import logout_user


def profile_page():

    if not st.session_state.logged_in:
        st.error("Please login first.")
        st.stop()

    st.title("👤 Profile")

    st.write("### User Details")

    st.write(f"**Name:** {st.session_state.user_name}")
    st.write(f"**Email:** {st.session_state.user_email}")

    if st.button("🚪 Logout"):

        logout_user()

        st.success("Logged out successfully.")

        st.rerun()