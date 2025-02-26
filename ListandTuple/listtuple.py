import csv
import os

# Global variable for storing records
students = []
filename = "students.csv"

def load_records():
    global students
    if os.path.exists(filename):
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            students = [tuple(row) for row in reader]
    else:
        print("No existing file found.")

def save_records():
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(students)

def save_as(new_filename):
    with open(new_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(students)
    print(f"Records saved as {new_filename}")

def show_all_records():
    for student in students:
        print(student)

def order_by_last_name():
    sorted_records = sorted(students, key=lambda x: x[1].split()[1])
    for student in sorted_records:
        print(student)

def order_by_grade():
    sorted_records = sorted(students, key=lambda x: (float(x[2]) * 0.6 + float(x[3]) * 0.4), reverse=True)
    for student in sorted_records:
        print(student)

def show_student_record(student_id):
    for student in students:
        if student[0] == student_id:
            print(student)
            return
    print("Student not found.")

def add_record():
    student_id = input("Enter Student ID (6-digit number): ")
    name = input("Enter Full Name: ")
    class_standing = input("Enter Class Standing Grade: ")
    major_exam = input("Enter Major Exam Grade: ")
    students.append((student_id, name, class_standing, major_exam))
    print("Record added successfully.")

def edit_record(student_id):
    for i, student in enumerate(students):
        if student[0] == student_id:
            name = input(f"Enter new name ({student[1]}): ") or student[1]
            class_standing = input(f"Enter new Class Standing ({student[2]}): ") or student[2]
            major_exam = input(f"Enter new Major Exam Grade ({student[3]}): ") or student[3]
            students[i] = (student_id, name, class_standing, major_exam)
            print("Record updated successfully.")
            return
    print("Student not found.")

def delete_record(student_id):
    global students
    students = [student for student in students if student[0] != student_id]
    print("Record deleted successfully.")

def main():
    load_records()
    while True:
        print("\nStudent Record Management System")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            load_records()
        elif choice == "2":
            save_records()
        elif choice == "3":
            new_filename = input("Enter new filename: ")
            save_as(new_filename)
        elif choice == "4":
            show_all_records()
        elif choice == "5":
            order_by_last_name()
        elif choice == "6":
            order_by_grade()
        elif choice == "7":
            student_id = input("Enter Student ID: ")
            show_student_record(student_id)
        elif choice == "8":
            add_record()
        elif choice == "9":
            student_id = input("Enter Student ID to edit: ")
            edit_record(student_id)
        elif choice == "10":
            student_id = input("Enter Student ID to delete: ")
            delete_record(student_id)
        elif choice == "11":
            save_records()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
