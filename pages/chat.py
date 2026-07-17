import streamlit as st

from database.database import SessionLocal

from chatbot.chat_service import (
    chatbot_response,
    save_conversation
)


def chat_page():

    if not st.session_state.logged_in:
        st.error("Please login first.")
        st.stop()

    st.title("🤖 AI Customer Support")

    # Clear Chat Button
    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    prompt = st.chat_input("Ask your question...")

    if prompt:

        # Show user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        # Connect to database
        db = SessionLocal()

        try:
            # Get AI response
            response = chatbot_response(prompt)

            # Save to MySQL
            save_conversation(
                db,
                st.session_state.user_id,
                prompt,
                response
            )

        except Exception as e:
            response = f"Error: {e}"

        finally:
            db.close()

        # Show AI response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        with st.chat_message("assistant"):
            st.markdown(response)