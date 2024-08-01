import numpy as np

def build_matrix_1():
    rows = int(input("Enter the number of rows for the first matrix:\n"))
    columns = int (input("Enter the number of columns for the first matrix:\n"))
    matrix = []
    print(f"Enter values for a {rows}x{columns} matrix:")
    for i in range(rows):
        rows_values = input(f"Enter {columns} values for row {i+1} (separated by space):\n")
        rows_values = [float(value) for value in rows_values.split()]
        matrix.append(rows_values)
    return np.array(matrix)

matrix_1=build_matrix_1()
print(f'''This is matrix 1:
{matrix_1}''')

def build_matrix_2():
    rows = int(input("Enter the number of rows for the second matrix:\n"))
    columns = int (input("Enter the number of columns for the second matrix:\n"))
    matrix = []
    print(f"Enter values for a {rows}x{columns} matrix:")
    for i in range(rows):
        rows_values = input(f"Enter {columns} values for row {i+1} (separated by space):\n")
        rows_values = [float(value) for value in rows_values.split()]
        matrix.append(rows_values)
    return np.array(matrix)

matrix_2=build_matrix_2()
print(f'''This is matrix 2:
{matrix_2}''')

try:
    matrix_sum = np.add(matrix_1,matrix_2)

    print("Matrix sum:")
    print(matrix_sum)

except ValueError:
    print("Error: sum not possible")

try:
    matrix_times = np.dot(matrix_1,matrix_2)

    print("Matrix multiplication:")
    print(matrix_times)

except ValueError:
    print("Error: multiplication not possible")
