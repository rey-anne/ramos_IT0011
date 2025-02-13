from datetime import datetime

# user input
date_input = input("Enter the date (mm/dd/yyyy): ")

try:
    # translate input string to a datetime object
    date_object = datetime.strptime(date_input, "%m/%d/%Y")
    
    # formatt date into a more readable format
    readable_date = date_object.strftime("%B %d, %Y")
    
    print(f"Date Output: {readable_date}")
except ValueError:
    print("Invalid date format! Please enter the date in mm/dd/yyyy format.")