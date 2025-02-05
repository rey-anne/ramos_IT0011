def pattern_a(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "".join(str(j) for j in range(1, i + 1)))

#usage
pattern_a(5)
