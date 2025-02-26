# Open the file in read mode
try:
    with open("students.txt", "r") as file:
        print("Reading student information:")
        
        # Read and display each line
        for line in file:
            data = line.strip().split(", ")
            if len(data) == 5:
                print(f"   Last name: {data[0]}")
                print(f"   First name: {data[1]}")
                print(f"   Age: {data[2]}")
                print(f"   Contact number: {data[3]}")
                print(f"   Course: {data[4]}")
                print()
except FileNotFoundError:
    print("Error: 'students.txt' not found.")
