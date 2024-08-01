
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
        
def main():
    rows = int(input("Enter the number of rows:\n"))
    cols = int(input("Enter the number of columns:\n"))

    matrix = create_matrix(rows, cols)
    print_matrix(matrix)
    
                            
main()
