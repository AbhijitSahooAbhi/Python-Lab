def get_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1} elements separated by space: ").split()))
        while len(row) != cols:
            print(f"Please enter exactly {cols} elements.")
            row = list(map(int, input(f"Enter row {i + 1} elements again: ").split()))
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    rows, cols = len(matrix1), len(matrix1[0])
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
    return result

def print_matrix(matrix, label):
    print(f"{label}:")
    for row in matrix:
        print(" ".join(map(str, row)))

# Taking input for matrix size
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Enter elements for first matrix:")
matrix1 = get_matrix(rows, cols)

print("Enter elements for second matrix:")
matrix2 = get_matrix(rows, cols)

# Printing input matrices
print_matrix(matrix1, "First Matrix")
print_matrix(matrix2, "Second Matrix")

# Adding matrices
result_matrix = add_matrices(matrix1, matrix2)

print("The resulting matrix after addition is:")
print_matrix(result_matrix, "Resultant Matrix")
