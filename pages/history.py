import streamlit as st

from database.database import SessionLocal
from database.crud import get_chat_history


def history_page():

    if not st.session_state.logged_in:
        st.error("Please login first.")
        st.stop()

    st.title("📜 Chat History")

    db = SessionLocal()

    chats = get_chat_history(
        db,
        st.session_state.user_id
    )

    db.close()

    if not chats:
        st.info("No chat history found.")
        return

    for chat in chats:

        st.chat_message("user").write(chat.question)

        st.chat_message("assistant").write(chat.answer)