def print_column(file_name):
    import csv
    
    my_file = open(file_name, 'r')

    for lines in my_file:
        col = lines.strip().split(",")

        if len(col) > 1:
            print(col[1].strip())

file_name = input("Give the name of the CSV file:\n")
print_column(file_name)
