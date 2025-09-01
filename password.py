# hash_my_password.py
import hashlib

# --- ENTER YOUR PASSWORD HERE ---
my_password = "karthik123"
# -----------------------------

hashed_password = hashlib.sha256(my_password.encode()).hexdigest()

print("Your username: karthik") # Or whatever your username is
print(f"Your hashed password (copy this into .env): {hashed_password}")