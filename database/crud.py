from sqlalchemy.orm import Session
from database.models import User


def get_user_by_email(db: Session, email: str):

    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def create_user(
    db: Session,
    full_name: str,
    email: str,
    password: str
):

    user = User(
        full_name=full_name,
        email=email,
        password=password
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user

from database.models import Chat


def save_chat(db, user_id, question, answer):

    chat = Chat(
        user_id=user_id,
        question=question,
        answer=answer
    )

    db.add(chat)

    db.commit()

    db.refresh(chat)

    return chat


def get_chat_history(db, user_id):

    return (
        db.query(Chat)
        .filter(Chat.user_id == user_id)
        .order_by(Chat.created_at.asc())
        .all()
    )