import tkinter as tk
from tkinter import filedialog
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    cipher = Cipher(algorithms.AES(key), modes.CFB8(), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()

    with open(file_path + '.enc', 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    cipher = Cipher(algorithms.AES(key), modes.CFB8(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    with open(file_path[:-4], 'wb') as file:
        file.write(decrypted_data)

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename()
    if file_path:
        key = input("Enter encryption key (must be 16, 24, or 32 bytes long): ").encode()
        
        encrypt_file(file_path, key)
        print("File encrypted successfully.")

        decrypt_file(file_path + '.enc', key)
        print("File decrypted successfully.")

def main():
    select_file()

if __name__ == "__main__":
    main()
