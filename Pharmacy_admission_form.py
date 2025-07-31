import tkinter as tk
from tkinter import messagebox

# Submit function
def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    course = course_var.get()
    email = entry_email.get()
    phone = entry_phone.get()
    
    if not name or not age or not email or not phone:
        messagebox.showwarning("Input Error", "Please fill all required fields.")
        return

    try:
        int(age)
        int(phone)
    except ValueError:
        messagebox.showerror("Input Error", "Age and Phone must be numeric.")
        return

    # Here you can save to a database or file
    messagebox.showinfo("Success", f"Admission submitted for {name}!")

# Main window
root = tk.Tk()
root.title("Pharmacy Admission Form")
root.geometry("400x500")
root.config(bg="#f0f0f0")

# Labels and Entries
tk.Label(root, text="Pharmacy Admission Form", font=("Arial", 16, 'bold'), bg="#f0f0f0").pack(pady=10)

tk.Label(root, text="Full Name *", bg="#f0f0f0").pack()
entry_name = tk.Entry(root, width=40)
entry_name.pack(pady=5)

tk.Label(root, text="Age *", bg="#f0f0f0").pack()
entry_age = tk.Entry(root, width=40)
entry_age.pack(pady=5)

tk.Label(root, text="Gender", bg="#f0f0f0").pack()
gender_var = tk.StringVar(value="Male")
tk.OptionMenu(root, gender_var, "Male", "Female", "Other").pack(pady=5)

tk.Label(root, text="Course", bg="#f0f0f0").pack()
course_var = tk.StringVar(value="B.Pharm")
tk.OptionMenu(root, course_var, "D.Pharm", "B.Pharm", "M.Pharm", "Pharm.D").pack(pady=5)

tk.Label(root, text="Email *", bg="#f0f0f0").pack()
entry_email = tk.Entry(root, width=40)
entry_email.pack(pady=5)

tk.Label(root, text="Phone *", bg="#f0f0f0").pack()
entry_phone = tk.Entry(root, width=40)
entry_phone.pack(pady=5)

# Submit Button
tk.Button(root, text="Submit", command=submit_form, bg="#4CAF50", fg="white", width=20).pack(pady=20)

# Run the app
root.mainloop()

