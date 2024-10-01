def matrix_inversion(matrix):
    n = len(matrix)
    identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    
    # Perform row operations to get the identity matrix on the left side
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


if __name__ == "__main__":
    matrix = [
        [1, 2],
        [3, 4],
    ]

    inverse = matrix_inversion(matrix)
    for row in inverse:
        print(row)