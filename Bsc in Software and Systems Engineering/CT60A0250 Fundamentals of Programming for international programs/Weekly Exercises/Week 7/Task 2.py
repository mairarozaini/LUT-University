def print_names(file_name):
    file_name = open(file_name,'r')
    l = []
    
    #names = (file_name.read())
    #print(names)
    line = file_name.readlines()
    for names in line:
        names.strip()
        l.append(names)
        
    l.sort()
    for name in l:
        print(name, end = '')
        
    file_name.close()

file_name1 = input("Give the name of the input file:\n") 
print_names(file_name1)
