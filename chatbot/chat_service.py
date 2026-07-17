from chatbot.gemini_service import ask_gemini
from database.crud import save_chat


def chatbot_response(question):

    try:
        response = ask_gemini(question)

    except Exception as e:
        response = f"Error: {str(e)}"

    return response


def save_conversation(db, user_id, question, answer):

    save_chat(
        db,
        user_id,
        question,
        answer
    )