from auth.password import hash_password
from auth.password import verify_password

password = "admin123"

hashed = hash_password(password)

print("Original :", password)
print("Hashed   :", hashed)

print()

print("Verify :", verify_password(
    "admin123",
    hashed
))