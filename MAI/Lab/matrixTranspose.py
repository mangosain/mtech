n = int(input("Enter the dimension of matrix: "))

matrix = []

# input matrix elements
for i in range(n):
    rows = []
    for j in range(n):
        value = int(input(f"Enter the {i}{j} element of the matrix: "))
        rows.append(value)
    matrix.append(rows)

# print original matrix
print("\nOriginal matrix:")
for row in matrix:
    print(row)

# swap the non diagonal elements
for i in range(len(matrix)):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# print transpose of original matrix
print("\nTransposed matrix:")
for row in matrix:
    print(row)