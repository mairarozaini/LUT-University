matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

while True:
    try:
        i = int(input("Enter the row index:\n"))
    except: 
        print("Error: Please enter valid integers for row and column indices.")
        break
    try:
        n = int(input("Enter the column index:\n"))
    except:
        print("Error: Please enter valid integers for row and column indices.")
        break
    try:
        print(f"Value at position ({i}, {n}): {matrix[i][n]}")
        break
    except:
        if i > 2 or n > 2 or i < 0 or n < 0:
            print("Error: Index out of bounds. Please enter valid row and column indices.")
            break