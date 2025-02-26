# Get user input
last_name = input("Last name: ")
first_name = input("First name: ")
age = input("Age: ")
contact_number = input("Contact Number: ")
course = input("Course: ")

# Format the student information
student_info = f"{last_name}, {first_name}, {age}, {contact_number}, {course}\n"

# Write to file in append mode
with open("students.txt", "a") as file:
    file.write(student_info)

# Display confirmation message
print("Student information has been saved to 'students.txt'.")
