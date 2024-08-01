sentence = input("Give a sentence:\n")

count_words = 0

for i in sentence:
    if i == " ":
        count_words += 1
count_words += 1
print(f"This sentence contains {count_words} words.")
