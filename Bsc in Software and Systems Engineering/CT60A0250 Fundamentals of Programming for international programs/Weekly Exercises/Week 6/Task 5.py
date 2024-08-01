def create_matrix(rows, cols):
    
    matrix = []
    
    for i in range(rows):
        row = []
        while len(row) < cols:
            input_rows = list(map(int, input(f"Give row {i+1}:\n").replace(" ", "")))
            if len(input_rows) == cols:
               # print(input_rows)
                row.extend(input_rows)
            else:
               # print(input_rows)
                print("Error: Invalid number of elements in the row. Please try again.")
                
        matrix.append(row)

   # print(matrix)    
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print("|", end="")
        print("\t".join(map(str, row)), end="")
        print("|")

def transpose(matrix):
    cols_number = len(matrix[0])
    rows_number = len(matrix)

# This 1 line code:
    transposed = [[0 for _ in range(rows_number)] for _ in range(cols_number)]

#Is the same as these 4 lines code:
#   transposed = []
#   for _ in range(cols_number):
#        row = [0] * rows_number
#        transposed.append(row)

    for i in range(rows_number):
        for j in range(cols_number):
            transposed[j][i] = matrix[i][j]
    return transposed
    
def main():
    rows = int(input("Enter the number of rows:\n"))
    cols = int(input("Enter the number of columns:\n"))
 
    matrix = create_matrix(rows, cols)
    print("The original matrix:")
    print_matrix(matrix)

    transposed_matrix = transpose(matrix)
    print("Its transpose:")
    print_matrix(transposed_matrix)
    
main()

