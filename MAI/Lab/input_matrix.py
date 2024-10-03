rows = int(input(f"Enter the rows of the matrix"))
cols = int(input(f"Enter the cols of the matrix"))
# matrix = [[int(input(f"Enter the {i}{j} element of the matrix")) for j in range(cols)] for i in range(rows)]

matrix = []

for i in range(rows):
    rows = []
    for j in range(cols):
        value = int(input(f"Enter the {i}{j} element of the matrix"))
        rows.append(value)
    matrix.append(rows)

print(matrix)
for row in matrix:
    print(row)