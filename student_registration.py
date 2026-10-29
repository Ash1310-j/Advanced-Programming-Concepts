import tkinter as tk
from tkinter import messagebox
import re

# Function to validate and register student
def register():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    course = course_var.get()

    # Check empty fields
    if name == "" or age == "" or email == "" or phone == "" or course == "Select Course":
        messagebox.showerror("Error", "All fields are required!")
        return

    # Validate name
    if not name.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Name must contain only letters!")
        return

    # Validate age
    if not age.isdigit() or not (16 <= int(age) <= 100):
        messagebox.showerror("Error", "Enter a valid age between 16 and 100!")
        return

    # Validate email
    if not re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email):
        messagebox.showerror("Error", "Enter a valid email address!")
        return

    # Validate phone number
    if not phone.isdigit() or len(phone) != 10:
        messagebox.showerror("Error", "Phone number must contain exactly 10 digits!")
        return

    # Registration successful
    messagebox.showinfo(
        "Success",
        f"Student Registered Successfully!\n\n"
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Email: {email}\n"
        f"Phone: {phone}\n"
        f"Course: {course}"
    )

# Create main window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x450")
root.configure(bg="lightblue")

# Heading
tk.Label(
    root,
    text="Student Registration Form",
    font=("Arial", 16, "bold"),
    bg="lightblue"
).pack(pady=15)

# Name
tk.Label(root, text="Full Name:", bg="lightblue").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Age
tk.Label(root, text="Age:", bg="lightblue").pack()
age_entry = tk.Entry(root, width=30)
age_entry.pack(pady=5)

# Email
tk.Label(root, text="Email:", bg="lightblue").pack()
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

# Phone
tk.Label(root, text="Phone Number:", bg="lightblue").pack()
phone_entry = tk.Entry(root, width=30)
phone_entry.pack(pady=5)

# Course selection
tk.Label(root, text="Select Course:", bg="lightblue").pack()

course_var = tk.StringVar(value="Select Course")

course_menu = tk.OptionMenu(
    root,
    course_var,
    "Computer Science",
    "Information Technology",
    "Mechanical Engineering",
    "Civil Engineering",
    "Electronics Engineering"
)
course_menu.pack(pady=5)

# Register button
tk.Button(
    root,
    text="Register",
    command=register,
    bg="green",
    fg="white",
    font=("Arial", 11, "bold")
).pack(pady=20)

# Run application
root.mainloop()

