import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def evaluate_strength(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) < 10:
        return "Medium"
    else:
        return "Strong"

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number for length.")
        return

    use_upper = var_upper.get()
    use_lower = var_lower.get()
    use_digits = var_digits.get()
    use_symbols = var_symbols.get()

    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        messagebox.showwarning("No Options Selected", "Please select at least one character type.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)
    strength_var.set(f"Strength: {evaluate_strength(password)}")
    pyperclip.copy(password)
    test_entry.delete(0, tk.END)
    messagebox.showinfo("Password Copied", "✅ Password copied to clipboard!\nPaste it below to test using Ctrl+V")

# GUI setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x400")
root.config(padx=20, pady=20)

# Title
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

# Length input
tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Checkboxes
var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase", variable=var_upper).pack(anchor='w')
tk.Checkbutton(root, text="Include Lowercase", variable=var_lower).pack(anchor='w')
tk.Checkbutton(root, text="Include Digits", variable=var_digits).pack(anchor='w')
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack(anchor='w')

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)

# Output password
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Courier", 12), justify='center', state='readonly').pack(pady=5)

# Strength
strength_var = tk.StringVar()
tk.Label(root, textvariable=strength_var, font=("Arial", 10, "italic")).pack()

# Ctrl+V test box
tk.Label(root, text="\nPaste Here to Test (Ctrl+V):").pack()
test_entry = tk.Entry(root, font=("Courier", 12), justify='center')
test_entry.insert(0, "ctrl+v")
test_entry.pack(pady=5)

# Run GUI
root.mainloop()
