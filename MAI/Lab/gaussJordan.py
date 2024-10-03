def gauss_jordan(augmented_matrix):
    n = len(augmented_matrix)
    m = len(augmented_matrix[0])

    # Forward elimination
    for i in range(n):
        # Make all elemets of the diagonal = 1
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

# main function
if __name__ == "__main__":
    # take input for number of rows
    n = int(input("Enter the number of rows for matrix: "))

    # take input for number of cols
    m = int(input("Enter the number of cols for the matrix: "))

    matrix = [[int(input(f"Enter the {i}x{j}th element: ")) for j in range(m)] for i in range(n)]

    # print original matrix
    print("\nOriginal Matrix:")
    for rows in matrix:
        print(rows)

    solution = gauss_jordan(matrix)
    print("\nSolution:", solution)