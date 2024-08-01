word_list = []

word1 = input("Enter word 1:\n")
word_list.append(word1)
word2 = input("Enter word 2:\n")
word_list.append(word2)

word_list.sort()

if (word1 == word2):
    print("The words are the same.")
else:
    print(f"'{word_list[0]}' comes earlier in order than '{word_list[1]}'.")


if ("z" in word1 and "z" in word2):
    print(f"""Letter 'z' is found in word '{word1}'.
Letter 'z' is found in word '{word2}'.""")
elif ("z" in word1):
    print(f"Letter 'z' is found in word '{word1}'.")
elif ("z" in word2):
    print(f"Letter 'z' is found in word '{word2}'.")
elif ("z" not in word1 and "z" not in word2):
    print("The letter 'z' was not found in either of the words.")

word3 = input("Enter a word to be tested:\n")

word4 = word3[::-1]

if (word3 == word4):
    print(f"'{word3}' is a palindrome.")
else:
     print(f"'{word3}' is not a palindrome.")
    
    
