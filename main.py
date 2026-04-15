password = input("Parol kiriting: ")

if len(password) >= 8 and any(c.isdigit() for c in password):
    print("Kuchli parol 💪")
else:
    print("Kuchsiz parol ❌")
