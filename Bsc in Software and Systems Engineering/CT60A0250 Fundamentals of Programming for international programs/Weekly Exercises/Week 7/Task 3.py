def file_copy(fileA, fileB):
    fileA = open(fileA, 'r')
    fileB = open(fileB, 'w')
    
    A_content = fileA.read()
    for content in A_content:
        fileB.write(content)
    fileA.close()
    fileB.close()

fileA = input("Please give the name of the source file:\n")
fileB = input("Please give the name of the destination file:\n")
print("File copied successfully!")
file_copy(fileA, fileB)
