🔐 Password Manager

Overview

This project is a local Password Manager developed in Python. It securely stores user credentials using encryption and allows users to manage passwords through a simple command-line interface.

Features

- Master Password Authentication
- Add Password Entries
- Retrieve Stored Passwords
- Delete Password Entries
- Search Password Entries
- Encrypted Password Storage
- Secure Local JSON Database
- AES-based Symmetric Encryption using Fernet

Technologies Used

- Python 3
- Cryptography Library (Fernet)
- JSON
- File Handling

Project Structure

password_manager.py

passwords.json

secret.key

README.md

Installation

1. Clone the repository:

git clone https://github.com/your-username/PasswordManager.git

2. Navigate to the project directory:

cd PasswordManager

3. Install required package:

pip install cryptography

Usage

Run the program:

python password_manager.py

Enter the master password to access the password manager.

Available options:

1. Add Password
2. Retrieve Password
3. Delete Password
4. Search Password
5. Exit

Security Features

- Passwords are encrypted before being stored.
- Encryption keys are managed separately.
- Credentials are stored locally on disk.
- Secure JSON-based storage format.
- Master password authentication protects access.

Example Storage Format

{
  "gmail": "gAAAAABxxxxxx...",
  "facebook": "gAAAAABxxxxxx..."
}

Learning Outcomes

- Cryptography and Encryption
- Secure Password Storage
- JSON Data Management
- Python File Handling
- Cybersecurity Fundamentals

Author

Dharshini R P

License

This project is developed for educational and internship evaluation purposes only. It is not intended for production use.
