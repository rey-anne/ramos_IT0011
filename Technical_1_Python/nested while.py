def pattern_b():
    i = 1
    while i <= 7:
        # Calculate the number of spaces for alignment
        spaces = (7 - i) // 2
        # Print spaces followed by the number repeated i times
        print(" " * spaces + str(i) * i)
        # Increment i by 2 to print only odd numbers (1, 3, 5, 7)
        i += 2

# Call the function to display the pattern
pattern_b()
