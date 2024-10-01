import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    # Get the user inputs from the GUI
    length = length_entry.get()
    
    # Validate length input
    if not length.isdigit() or int(length) <= 0:
        messagebox.showerror("Invalid Input", "Password length must be a positive integer.")
        return
    
    length = int(length)
    
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()

    # Pool of characters based on user preferences
    characters = ''
    password = []
    
    if include_lowercase:
        characters += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))  # Ensure at least one lowercase letter
    if include_uppercase:
        characters += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))  # Ensure at least one uppercase letter
    if include_digits:
        characters += string.digits
        password.append(random.choice(string.digits))  # Ensure at least one digit
    if include_special:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))  # Ensure at least one special character
    
    # If no character type is selected, show an error message
    if not characters:
        messagebox.showerror("No Selection", "You must select at least one character type.")
        return

    # Fill the rest of the password length with random characters from the selected pool
    password += [random.choice(characters) for _ in range(length - len(password))]
    
    # Shuffle the password for randomness
    random.shuffle(password)
    
    # Display the generated password
    password_display.config(text="Generated Password: " + ''.join(password))

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Password length label and input field
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Checkboxes for character options
lowercase_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

lowercase_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_check.pack()

uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.pack()

digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.pack()

special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_check.pack()

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=20)

# Label to display the generated password
password_display = tk.Label(root, text="")
password_display.pack(pady=10)

# Run the application
root.mainloop()
