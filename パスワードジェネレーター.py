import random
import string

def generate_password(length=12, use_symbols=True):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("--- 簡易パスワードジェネレーター ---")
for i in range(5):
    pwd = generate_password(length=16)
    print(f"候補 {i+1}: {pwd}")
print("------------------------------")
