import re
import hashlib

# re checks letters, numbers, and symbols
# hashlib converts plain text to hashed data

password = input("Enter your password: ")

strength = 0

if len(password) >= 8:
    strength += 1

if re.search("[A-Z]", password):
    strength += 1

if re.search("[a-z]", password):
    strength += 1

if re.search("[0-9]", password):
    strength += 1

if re.search("[!@#$%^&*]", password):
    strength += 1

if strength <= 2:
    print("Password Strength: WEAK")
elif strength <= 4:
    print("Password Strength: MEDIUM")
else:
    print("Password Strength: STRONG")

# Hashing must be OUTSIDE all if blocks
hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("Hashed Password:", hashed_password)
