# Example 6-1: Creating and writing the following text to  file myfile.txt
file_name = "myfile.txt"
file=open(file_name, "w")
wstr="First line!\nSecond line!\nLast in line!\n"
file.write(wstr)
print("File '" + file_name + "' written. Bye!")
file.close()
