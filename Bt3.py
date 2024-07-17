import tkinter as tk
from tkinter import ttk, messagebox

class DataEntryForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Entry Form")
        self.root.geometry("500x400")

        # Khung thông tin người dùng
        self.user_info_frame = ttk.LabelFrame(root, text="User Information")
        self.user_info_frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(self.user_info_frame, text="First Name").grid(row=0, column=0, padx=5, pady=5)
        self.first_name_entry = ttk.Entry(self.user_info_frame)
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.user_info_frame, text="Last Name").grid(row=0, column=2, padx=5, pady=5)
        self.last_name_entry = ttk.Entry(self.user_info_frame)
        self.last_name_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(self.user_info_frame, text="Title").grid(row=0, column=4, padx=5, pady=5)
        self.title_combobox = ttk.Combobox(self.user_info_frame, values=["Mr.", "Mrs.", "Miss", "Dr."])
        self.title_combobox.grid(row=0, column=5, padx=5, pady=5)

        ttk.Label(self.user_info_frame, text="Age").grid(row=1, column=0, padx=5, pady=5)
        self.age_spinbox = ttk.Spinbox(self.user_info_frame, from_=0, to=100)
        self.age_spinbox.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.user_info_frame, text="Nationality").grid(row=1, column=2, padx=5, pady=5)
        self.nationality_entry = ttk.Entry(self.user_info_frame)
        self.nationality_entry.grid(row=1, column=3, padx=5, pady=5)

        # Khung trạng thái đăng ký
        self.registration_frame = ttk.LabelFrame(root, text="Registration Status")
        self.registration_frame.pack(padx=10, pady=10, fill="x")

        self.registered_var = tk.BooleanVar()
        self.registered_checkbutton = ttk.Checkbutton(self.registration_frame, text="Currently Registered", variable=self.registered_var)
        self.registered_checkbutton.grid(row=0, column=0, padx=5, pady=5)

        ttk.Label(self.registration_frame, text="# Completed Courses").grid(row=0, column=1, padx=5, pady=5)
        self.completed_courses_spinbox = ttk.Spinbox(self.registration_frame, from_=0, to=50)
        self.completed_courses_spinbox.grid(row=0, column=2, padx=5, pady=5)

        ttk.Label(self.registration_frame, text="# Semesters").grid(row=0, column=3, padx=5, pady=5)
        self.semesters_spinbox = ttk.Spinbox(self.registration_frame, from_=0, to=12)
        self.semesters_spinbox.grid(row=0, column=4, padx=5, pady=5)

        # Khung điều khoản và điều kiện
        self.terms_frame = ttk.LabelFrame(root, text="Terms & Conditions")
        self.terms_frame.pack(padx=10, pady=10, fill="x")

        self.terms_var = tk.BooleanVar()
        self.terms_checkbutton = ttk.Checkbutton(self.terms_frame, text="I accept the terms and conditions.", variable=self.terms_var)
        self.terms_checkbutton.pack(padx=5, pady=5)

        # Nút gửi
        self.submit_button = ttk.Button(root, text="Enter data", command=self.submit_data)
        self.submit_button.pack(pady=20)

    def submit_data(self):
        if self.terms_var.get():
            user_data = {
                "First Name": self.first_name_entry.get(),
                "Last Name": self.last_name_entry.get(),
                "Title": self.title_combobox.get(),
                "Age": self.age_spinbox.get(),
                "Nationality": self.nationality_entry.get(),
                "Currently Registered": self.registered_var.get(),
                "# Completed Courses": self.completed_courses_spinbox.get(),
                "# Semesters": self.semesters_spinbox.get(),
            }
            messagebox.showinfo("Submitted Data", f"User Data:\n{user_data}")
            print("User Data:", user_data)
        else:
            messagebox.showwarning("Terms Not Accepted", "You must accept the terms and conditions to submit the data.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataEntryForm(root)
    root.mainloop()
