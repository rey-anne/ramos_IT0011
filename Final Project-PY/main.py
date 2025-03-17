import tkinter as tk
from tkinter import messagebox
import json
import datetime

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def signup():
    def submit_signup():
        try:
            first_name = first_name_entry.get()
            middle_name = middle_name_entry.get()
            last_name = last_name_entry.get()
            birthday_str = birthday_entry.get()
            gender = gender_var.get()

            #hbd validation
            datetime.datetime.strptime(birthday_str, "%Y-%m-%d")

            data = load_data()
            new_record = {
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
                "birthday": birthday_str,
                "gender": gender,
            }
            data.append(new_record)
            save_data(data)
            messagebox.showinfo("Success", "Record added successfully.")
            signup_window.destroy()

        except ValueError:
            messagebox.showerror("Error", "Invalid birthday format (YYYY-MM-DD).")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")

    tk.Label(signup_window, text="First Name:").grid(row=0, column=0)
    first_name_entry = tk.Entry(signup_window)
    first_name_entry.grid(row=0, column=1)

    tk.Label(signup_window, text="Middle Name:").grid(row=1, column=0)
    middle_name_entry = tk.Entry(signup_window)
    middle_name_entry.grid(row=1, column=1)

    tk.Label(signup_window, text="Last Name:").grid(row=2, column=0)
    last_name_entry = tk.Entry(signup_window)
    last_name_entry.grid(row=2, column=1)

    tk.Label(signup_window, text="Birthday (YYYY-MM-DD):").grid(row=3, column=0)
    birthday_entry = tk.Entry(signup_window)
    birthday_entry.grid(row=3, column=1)

    tk.Label(signup_window, text="Gender:").grid(row=4, column=0)
    gender_var = tk.StringVar(signup_window)
    gender_var.set("Male")  #def val, diko alam pano alisin
    gender_menu = tk.OptionMenu(signup_window, gender_var, "Male", "Female", "Other")
    gender_menu.grid(row=4, column=1)

    tk.Button(signup_window, text="Submit", command=submit_signup).grid(row=5, column=0, columnspan=2)

def view_records():
    data = load_data()
    if not data:
        messagebox.showinfo("Info", "No records found.")
        return

    records_window = tk.Toplevel(root)
    records_window.title("View Records")

    text_area = tk.Text(records_window, width=50, height=10)
    text_area.pack()

    for record in data:
        text_area.insert(tk.END, f"First Name: {record['first_name']}\n")
        text_area.insert(tk.END, f"Middle Name: {record['middle_name']}\n")
        text_area.insert(tk.END, f"Last Name: {record['last_name']}\n")
        text_area.insert(tk.END, f"Birthday: {record['birthday']}\n")
        text_area.insert(tk.END, f"Gender: {record['gender']}\n")
        text_area.insert(tk.END, "-" * 20 + "\n")

def search_record():
    def perform_search():
        search_term = search_entry.get().lower()
        data = load_data()
        found_records = [
            record for record in data if search_term in record["first_name"].lower() or search_term in record["last_name"].lower()
        ]

        if not found_records:
            messagebox.showinfo("Info", "No matching records found.")
            return

        results_window = tk.Toplevel(search_window)
        results_window.title("Search Results")

        text_area = tk.Text(results_window, width=50, height=10)
        text_area.pack()

        #porda record
        for record in found_records:
            text_area.insert(tk.END, f"First Name: {record['first_name']}\n")
            text_area.insert(tk.END, f"Middle Name: {record['middle_name']}\n")
            text_area.insert(tk.END, f"Last Name: {record['last_name']}\n")
            text_area.insert(tk.END, f"Birthday: {record['birthday']}\n")
            text_area.insert(tk.END, f"Gender: {record['gender']}\n")
            text_area.insert(tk.END, "-" * 20 + "\n")

    search_window = tk.Toplevel(root)
    search_window.title("Search Record")

    tk.Label(search_window, text="Search Term:").pack()
    search_entry = tk.Entry(search_window)
    search_entry.pack()

    tk.Button(search_window, text="Search", command=perform_search).pack()

root = tk.Tk()
root.title("My Program")

menu_frame = tk.Frame(root)
menu_frame.pack(pady=20)

tk.Button(menu_frame, text="Sign Up", command=signup).grid(row=0, column=0, padx=10)
tk.Button(menu_frame, text="View Records", command=view_records).grid(row=0, column=1, padx=10)
tk.Button(menu_frame, text="Search Record", command=search_record).grid(row=0, column=2, padx=10)
tk.Button(menu_frame, text="Exit", command=root.quit).grid(row=0, column=3, padx=10)

root.mainloop()