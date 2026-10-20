# Write a program to demonstrate Functional Data Filtering & Matrix Transformation Suite.
# Original matrix
matrix = [
    [4, -2, 7],
    [3, -5, 1],
    [8, 6, -1]
]

print("Original Matrix:")
for row in matrix:
    print(row)

# 1. Remove negative values using filter() and lambda
positive_matrix = [
    list(filter(lambda x: x >= 0, row))
    for row in matrix
]

print("\nMatrix after removing negative values:")
for row in positive_matrix:
    print(row)

# 2. Square each element using map() and lambda
squared_matrix = [
    list(map(lambda x: x ** 2, row))
    for row in positive_matrix
]

print("\nSquared Matrix:")
for row in squared_matrix:
    print(row)

# 3. Sort each row in ascending order
sorted_matrix = [
    sorted(row, key=lambda x: x)
    for row in positive_matrix
]

print("\nSorted Matrix:")
for row in sorted_matrix:
    print(row)

# 4. Convert matrix rows into tuples
tuple_matrix = tuple(tuple(row) for row in sorted_matrix)

print("\nMatrix as Tuples:")
print(tuple_matrix)

# 5. Calculate sum of all positive elements
total = sum(map(sum, positive_matrix))

print("\nSum of positive elements:", total)