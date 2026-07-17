from sqlalchemy import text

from database.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT VERSION();"))

        version = result.fetchone()

        print("=" * 50)
        print("Database Connected Successfully!")
        print("MySQL Version:", version[0])
        print("=" * 50)

except Exception as e:
    print("Connection Failed!")
    print(e)