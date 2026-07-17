from database.models import User

user = User(
    full_name="Sowmiya",
    email="test@gmail.com",
    password="123456"
)

print(user.full_name)
print(user.email)