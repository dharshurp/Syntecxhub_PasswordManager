# Syntecxhub_PasswordManager
# 🔐 Secure Password Manager

## 📌 Project Overview
This project is a Secure Password Manager developed using Python and Fernet Encryption. It allows users to securely store, retrieve, and delete passwords while keeping sensitive information encrypted on local storage.

## 🎯 Objectives
- Store passwords securely
- Protect credentials using encryption
- Learn cybersecurity concepts and secure coding practices
- Practice Python file handling and data management

## ⚙️ Technologies Used
- Python
- Cryptography (Fernet)
- JSON
- File Handling

## ✨ Features
- Add Password
- View Password
- Delete Password
- Encrypted Password Storage
- Simple User Interface (Command Line)

## 🔒 Security Features
- Passwords are encrypted before storage
- Encryption key stored separately
- Secure local credential management

## 🚀 How to Run

1. Install required library:
   ```bash
   pip install cryptography
   ```

2. Generate encryption key:
   ```python
   from cryptography.fernet import Fernet

   key = Fernet.generate_key()
   with open("key.key", "wb") as f:
       f.write(key)
   ```

3. Run the Password Manager program.

## 📸 Output Screenshots
Add your screenshots here:
- Main Menu
- Add Password
- View Password
- Delete Password

## 👩‍💻 Author
Dharshini R P

## 🏢 Internship
Project completed as part of the Syntecxhub Cybersecurity Internship.
