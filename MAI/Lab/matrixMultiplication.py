def matrix_multiplication(matrix1, matrix2):
    # Initialize the result matrix
    result = [[0 for _ in range(m2)] for _ in range(n1)]

    # matrix multiplication
    for i in range(n1):
        for j in range(m2):
            for k in range(m1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# main function
if __name__ == "__main__":
    matrix1 = []
    matrix2 = []

    n1 = int(input("Enter the number of rows for 1st matrix: "))
    m1 = int(input("Enter the number of cols for 1st matrix: "))

    n2 = int(input("Enter the number of rows for 2nd matrix: "))
    m2 = int(input("Enter the number of cols for 2nd matrix: "))

    # take input for 1st matrix
    matrix1 = [[int(input(f"Enter the {i}{j} element of the matrix: ")) for j in range(m1)] for i in range(n1)]
    print("1st matrix: ")
    for rows in matrix1:
        print(rows)

    # take input for 1st matrix
    matrix2 = [[int(input(f"Enter the {i}{j} element of the matrix: ")) for j in range(m2)] for i in range(n2)]
    print("2nd matrix: ")
    for rows in matrix2:
        print(rows)

    # check if multiplication is possible
    if m1 != n2:
        raise ValueError("Matrices cannot be multiplied")

    result = matrix_multiplication(matrix1, matrix2)
    print("resultant matrix: ")
    for row in result:
        print(row)