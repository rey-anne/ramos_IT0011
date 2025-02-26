def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
        for index, line in enumerate(lines, start=1):
            numbers = list(map(int, line.strip().split(',')))
            total = sum(numbers)
            result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
            print(f"Line {index}: {', '.join(map(str, numbers))} (sum {total}) - {result}")
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid data format in file.")

# Run the function with the filename
process_file("numbers.txt")
