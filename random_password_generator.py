import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

# Function to generate a password
def generate_password():
    length = length_entry.get()

    if not length.isdigit() or int(length) <= 0:
        messagebox.showerror("Invalid Input", "Password length must be a positive integer.")
        return

    length = int(length)
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()

    characters = ''
    password = []

    if include_lowercase:
        characters += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
    if include_uppercase:
        characters += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if include_digits:
        characters += string.digits
        password.append(random.choice(string.digits))
    if include_special:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))

    if not characters:
        messagebox.showerror("No Selection", "Please select at least one character type.")
        return

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    generated_password = ''.join(password)

    password_display.delete(0, tk.END)
    password_display.insert(0, generated_password)

    update_strength_indicator(generated_password)

# Function to update the password strength indicator
def update_strength_indicator(password):
    strength_label.config(text=f"Strength: {evaluate_strength(password)}")
    strength_value = evaluate_strength_score(password)
    strength_bar["value"] = strength_value

# Function to evaluate strength
def evaluate_strength(password):
    length = len(password)
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    score = sum([has_lower, has_upper, has_digit, has_special])

    if length >= 12 and score == 4:
        return "Strong"
    elif length >= 8 and score >= 3:
        return "Moderate"
    else:
        return "Weak"

# Function to get score for progress bar
def evaluate_strength_score(password):
    return len(password) * 8 if evaluate_strength(password) == "Strong" else len(password) * 5

# Function to copy the password
def copy_password():
    password = password_display.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Function to toggle dark mode
def toggle_dark_mode():
    if style.theme_use() == "clam":
        style.theme_use("alt")
    else:
        style.theme_use("clam")

# Create main window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("600x400")
root.resizable(False, False)

style = ttk.Style(root)
style.theme_use("clam")

# Title
title_label = ttk.Label(root, text="Password Generator", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Frame for length input
length_frame = ttk.Frame(root)
length_frame.pack(pady=10, fill="x")

length_label = ttk.Label(length_frame, text="Enter Password Length:", font=("Arial", 12))
length_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

length_entry = ttk.Entry(length_frame, width=10)
length_entry.grid(row=0, column=1, padx=10, pady=5)

# Frame for options
options_frame = ttk.LabelFrame(root, text="Character Options", padding=(10, 5))
options_frame.pack(pady=10, fill="x")

lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=False)

lowercase_check = ttk.Checkbutton(options_frame, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_check.grid(row=0, column=0, sticky="w", padx=10)

uppercase_check = ttk.Checkbutton(options_frame, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.grid(row=1, column=0, sticky="w", padx=10)

digits_check = ttk.Checkbutton(options_frame, text="Include Digits", variable=digits_var)
digits_check.grid(row=2, column=0, sticky="w", padx=10)

special_check = ttk.Checkbutton(options_frame, text="Include Special Characters", variable=special_var)
special_check.grid(row=3, column=0, sticky="w", padx=10)

# Frame for password display and buttons
output_frame = ttk.Frame(root, padding=10)
output_frame.pack(pady=10, fill="x")

password_display = ttk.Entry(output_frame, width=50, font=("Arial", 12))
password_display.pack(pady=5)

button_frame = ttk.Frame(output_frame)
button_frame.pack()

generate_button = ttk.Button(button_frame, text="Generate Password", command=generate_password)
generate_button.grid(row=0, column=0, padx=10)

copy_button = ttk.Button(button_frame, text="Copy Password", command=copy_password)
copy_button.grid(row=0, column=1, padx=10)

# Strength indicator
strength_frame = ttk.Frame(root, padding=10)
strength_frame.pack(fill="x")

strength_label = ttk.Label(strength_frame, text="Strength: ", font=("Arial", 12))
strength_label.pack(side="left")

strength_bar = ttk.Progressbar(strength_frame, orient="horizontal", mode="determinate", length=300)
strength_bar.pack(side="right", padx=10)

# Toggle dark mode button
dark_mode_button = ttk.Button(root, text="Toggle Dark Mode", command=toggle_dark_mode)
dark_mode_button.pack(pady=10)

# Run the application
root.mainloop()
