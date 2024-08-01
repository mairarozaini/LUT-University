#Program1
file=open("filename FileEx1.txt","r")
contents = file.read()
print(contents)
file.close()
#Program2
with open("filename FileEx1.txt","r")as file:
    contents=file.read()
print(contents)
#Program3
file=open("filename FileEx1.txt","r")
contents=file.read(10)
print(contents)
file.close()
