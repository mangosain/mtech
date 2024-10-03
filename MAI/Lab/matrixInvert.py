def matrix_inversion(matrix):
    n = len(matrix)
    identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    
    # Perform row operations to get the identity matrix 
    for i in range(n):
        # Normalize the diagonal element
        divisor = matrix[i][i]
        for j in range(n):
            matrix[i][j] /= divisor
            identity[i][j] /= divisor
        
        # Eliminate other rows
        for j in range(n):
            if j != i:
                factor = matrix[j][i]
                for k in range(n):
                    matrix[j][k] -= factor * matrix[i][k]
                    identity[j][k] -= factor * identity[i][k]
    
    return identity

# main fucntion
if __name__ == "__main__":
    # take input for nxn
    n = int(input("Enter the dimension for matrix: "))

    matrix = [[int(input(f"Enter the {i}x{j}th element: ")) for j in range(n)] for i in range(n)]

    # print original matrix
    print("\nOriginal Matrix:")
    for rows in matrix:
        print(rows)

    inverse = matrix_inversion(matrix)
    print("\nInverse of the original matrix:")
    for row in inverse:
        print(row)