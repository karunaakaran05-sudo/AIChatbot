import streamlit as st


def home_page():

    st.title("🤖 AI Customer Support Chatbot")

    if st.session_state.logged_in:

        st.success(
            f"Welcome, {st.session_state.user_name}!"
        )

        st.write("You are logged in and can access all features.")

    else:

        st.info(
            "Please login or register to continue."
        )