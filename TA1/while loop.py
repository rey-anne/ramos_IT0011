print("\nA")
for i in range(1, 6):
    for space in range(5 - i):
        print(" ", end="")
    for num in range(1, i + 1):
        print(num, end="")
    print()


print("\nB")
i = 1
while i <= 7:
    count = 0
    while count < i:
        print(i, end="")
        count += 1
    print()
    if i == 1:
        i = 3
    elif i == 3:
        i = 5
    elif i == 5:
        i = 6
    elif i == 6:
        i = 7
    else:
        break