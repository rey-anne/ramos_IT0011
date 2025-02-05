def count_chars(string):
    vowels = consonants = spaces = others = 0
    for ch in string:
        if ch.lower() in "aeiou":
            vowels += 1
        elif ch.isalpha():
            consonants += 1
        elif ch.isspace():
            spaces += 1
        else:
            others += 1
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Spaces:", spaces)
    print("Other Characters:", others)

#usage
string = input("Enter a string: ")
count_chars(string)
