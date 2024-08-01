word = input("Enter a long word:\n")

first_five = word[:5]
print(f"The first five letters are: {first_five}")

last_five = word[-5::]
print(f"The last five letters are: {last_five}")

letters = word[1:5]
print(f"Letters 2, 3, 4 and 5 are: {letters}")

sec_letters = word[1::2]
print(f"Every second letter of the word: {sec_letters}")

backwards = word[::-1]
print(f"The word backwards '{backwards}'")

