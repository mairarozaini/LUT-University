def print_column(file_name):
    import csv
    
    my_file = open(file_name, 'r')
    csvreader = csv.reader(my_file)

    for col in csvreader:
        print(col[1].strip())

file_name = input("Give the name of the CSV file:\n")
print_column(file_name)
