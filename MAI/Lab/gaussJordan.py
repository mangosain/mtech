def gauss_jordan(augmented_matrix):
    n = len(augmented_matrix)
    m = len(augmented_matrix[0])

    # Forward elimination
    for i in range(n):
        # Make the diagonal contain all 1s
        divisor = augmented_matrix[i][i]
        for j in range(i, m):
            augmented_matrix[i][j] /= divisor
        
        # Eliminate other rows
        for j in range(n):
            if j != i:
                factor = augmented_matrix[j][i]
                for k in range(i, m):
                    augmented_matrix[j][k] -= factor * augmented_matrix[i][k]

    # Extracting the solution
    solution = [augmented_matrix[i][-1] for i in range(n)]
    return solution

# Example usage
if __name__ == "__main__":
    augmented_matrix = [
        [-1, -3, -1, 1, -7],
        [1, -4, -3, -4, -3],
        [1, 5, 2, 6, -3],
        [10, 4, -2, -2, 6],
    ]

    solution = gauss_jordan(augmented_matrix)
    print("Solution:", solution)
