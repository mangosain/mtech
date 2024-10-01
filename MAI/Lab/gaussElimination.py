def gauss_elimination(augmented_matrix):
    n = len(augmented_matrix)

    # Forward elimination
    for i in range(n):
        for j in range(i + 1, n):
            factor = augmented_matrix[j][i] / augmented_matrix[i][i]
            for k in range(i, n + 1):
                augmented_matrix[j][k] -= factor * augmented_matrix[i][k]

    # Back substitution
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = augmented_matrix[i][n]
        for j in range(i + 1, n):
            solution[i] -= augmented_matrix[i][j] * solution[j]
        solution[i] /= augmented_matrix[i][i]

    return solution

# Example usage
if __name__ == "__main__":
    # Example augmented matrix
    augmented_matrix = [
        [-1, -3, -1, 1, -7],
        [1, -4, -3, -4, -3],
        [1, 5, 2, 6, -3],
        [10, 4, -2, -2, 6],
    ]

    solution = gauss_elimination(augmented_matrix)
    print("Solution:", solution)
