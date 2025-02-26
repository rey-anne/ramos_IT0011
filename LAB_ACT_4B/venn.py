# Define the sets based on the given diagram
A = {'a', 'g', 'b', 'd', 'f', 'c'}
B = {'l', 'm', 'o', 'b', 'h', 'c'}
C = {'k', 'i', 'j', 'h', 'd', 'f', 'c'}

# a. How many elements are there in both A and B (intersection)
elements_in_A_and_B = A & B
print("a:", len(elements_in_A_and_B))

# b. How many elements are there in B that is not part of A and C
elements_in_B_not_A_or_C = B - (A | C)
print("b:", len(elements_in_B_not_A_or_C))

# c. Show the following using set operations
i = C - A  # [h, i, j, k]
ii = C & A  # [c, d, f]
iii = (B & C) | {'b'}  # [b, c, h]
iv = A & C - {'c'}  # [d, f]
v = C & {'c'}  # [c]
vi = B - (A | C)  # [l, m, o]

# Print results
print("i:", i)
print("ii:", ii)
print("iii:", iii)
print("iv:", iv)
print("v:", v)
print("vi:", vi)
