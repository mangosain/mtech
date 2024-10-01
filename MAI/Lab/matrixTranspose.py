# Code for matrix transpose

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Original matrix:")
for row in matrix:
    print(row)
    
print("\nTransposed matrix:")

for i in range(len(matrix)):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
for row in matrix:
    print(row)