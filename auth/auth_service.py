from sqlalchemy.orm import Session

from database.crud import get_user_by_email
from database.crud import create_user
from auth.password import hash_password, verify_password


def register_user(
    db: Session,
    full_name: str,
    email: str,
    password: str
):

    # Check existing email
    existing_user = get_user_by_email(db, email)

    if existing_user:
        return False, "Email already exists."

    # Hash password
    hashed_password = hash_password(password)

    # Save user
    create_user(
        db,
        full_name,
        email,
        hashed_password
    )

    return True, "Registration Successful."

def login_user(db, email, password):

    print("Email:", email)

    user = get_user_by_email(db, email)

    print("User:", user)

    if not user:
        return False, "Email not found.", None

    print("Database Password:", user.password)

    result = verify_password(password, user.password)

    print("Verify Result:", result)

    if not result:
        return False, "Invalid Password.", None

    return True, "Login Successful.", user