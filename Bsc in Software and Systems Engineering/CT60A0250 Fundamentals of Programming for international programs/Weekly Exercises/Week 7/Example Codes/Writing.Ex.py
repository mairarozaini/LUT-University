#Write a file
with open("filename FileEx1.txt","w")as optfile:
    optfile.write("I Love Python")
optfile.close()
#Write a file
lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    f.write('\n'.join(lines))
