from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from sqlalchemy import Text
from sqlalchemy.orm import relationship

from database.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    chats = relationship(
    "Chat",
    back_populates="user",
    cascade="all, delete"
)

   
class Chat(Base):

    __tablename__ = "chats"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    question = Column(Text, nullable=False)

    answer = Column(Text, nullable=False)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    user = relationship(
        "User",
        back_populates="chats"
    )