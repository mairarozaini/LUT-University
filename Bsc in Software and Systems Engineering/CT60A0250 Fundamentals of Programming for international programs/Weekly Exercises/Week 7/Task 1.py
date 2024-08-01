
def write_names(file_name):
    with open(f'{file_name}', 'a') as f:
        while True:
            name = input("Enter a name or 'stop':\n")
            if name.lower() != 'stop':
                f.write(name + '\n')
            else:
                break
    f.close()

file_name1 = input("Enter the name of the file to be saved:\n") 
write_names(file_name1)


