def gauss_elimination(matrix):
    n = len(matrix)

    # Forward elimination process
    for i in range(n):
        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= factor * matrix[i][k]

    # Back substitution process
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = matrix[i][n]
        for j in range(i + 1, n):
            solution[i] -= matrix[i][j] * solution[j]
        solution[i] /= matrix[i][i]

    return solution

# main funciton
if __name__ == "__main__":
    # take input for number of rows
    n = int(input("Enter the number of rows for matrix: "))
    # take input for number of cols
    m = int(input("Enter the number of cols for matrix: "))

    matrix = [[int(input(f"Enter the {i}x{j}th element: ")) for j in range(m)] for i in range(n)]

    # print original matrix
    print("\nOriginal Matrix:")
    for rows in matrix:
        print(rows)

    solution = gauss_elimination(matrix)
    print("\nSolution:", solution)
