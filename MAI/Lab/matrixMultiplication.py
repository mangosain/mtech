def matrix_multiplication(matrix1, matrix2):
    n1, m1 = len(matrix1), len(matrix1[0])
    n2, m2 = len(matrix2), len(matrix2[0])

    # Check if the matrices can be multiplied
    if m1 != n2:
        raise ValueError("Matrices cannot be multiplied")

    # Initialize the result matrix
    result = [[0 for _ in range(m2)] for _ in range(n1)]

    # Perform matrix multiplication
    for i in range(n1):
        for j in range(m2):
            for k in range(m1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Example usage
if __name__ == "__main__":
    matrix1 = [
        [1, 2],
        [3, 4],
    ]

    matrix2 = [
        [1],
        [2],
    ]

    result = matrix_multiplication(matrix1, matrix2)
    for row in result:
        print(row)