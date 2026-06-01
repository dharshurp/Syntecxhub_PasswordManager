import json
import os
from cryptography.fernet import Fernet

MASTER_PASSWORD = "admin123"
DATA_FILE = "passwords.json"
KEY_FILE = "secret.key"

def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)

    with open(KEY_FILE, "rb") as file:
        return file.read()

key = load_key()
cipher = Fernet(key)

def load_passwords():
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_passwords(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_password():
    site = input("Enter site name: ")
    password = input("Enter password: ")

    encrypted = cipher.encrypt(password.encode()).decode()

    data = load_passwords()
    data[site] = encrypted
    save_passwords(data)

    print("Password saved successfully!")

def retrieve_password():
    site = input("Enter site name: ")

    data = load_passwords()

    if site in data:
        decrypted = cipher.decrypt(data[site].encode()).decode()
        print("Password:", decrypted)
    else:
        print("Site not found!")

def delete_password():
    site = input("Enter site name: ")

    data = load_passwords()

    if site in data:
        del data[site]
        save_passwords(data)
        print(" Password deleted!")
    else:
        print(" Site not found!")

def search_password():
    keyword = input("Search site: ").lower()

    data = load_passwords()

    found = False

    for site in data:
        if keyword in site.lower():
            print("correct", site)
            found = True

    if not found:
        print("No matching site found.")

def login():
    password = input("Enter Master Password: ")

    if password == MASTER_PASSWORD:
        print(" Access Granted")
        return True

    print(" Wrong Password")
    return False


if login():

    while True:

        print("\n===== PASSWORD MANAGER =====")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Delete Password")
        print("4. Search Password")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_password()

        elif choice == "2":
            retrieve_password()

        elif choice == "3":
            delete_password()

        elif choice == "4":
            search_password()

        elif choice == "5":
            print("Exiting")
            break

        else:
            print(" Invalid Choice")