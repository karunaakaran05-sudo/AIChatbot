import bcrypt


def hash_password(password: str) -> str:
    """
    Convert plain password into hashed password.
    """

    password_bytes = password.encode("utf-8")

    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(password_bytes, salt)

    return hashed.decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify entered password with stored hashed password.
    """

    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )