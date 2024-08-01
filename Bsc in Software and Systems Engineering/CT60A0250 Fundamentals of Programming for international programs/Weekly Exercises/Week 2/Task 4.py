word = input("Give a word:\n")

length = len(word)
print(f"The length of the word is {length}")

integer = int(input(f"Give an integer smaller than or equal to {length}:\n"))

replace = integer - 1

print(word.replace(word[replace],'*'))




