def sum_digits(string):
    total = 0
    for ch in string:
        if ch.isdigit():
            total += int(ch)
    print("Sum of digits:", total)

#usage
string = input("Enter a string with digits: ")
sum_digits(string)
