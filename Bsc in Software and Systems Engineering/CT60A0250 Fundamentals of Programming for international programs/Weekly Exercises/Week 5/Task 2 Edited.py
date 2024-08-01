def count_words(sentence):

    words = 0

    for ch in sentence:
        if ch == " ":
            words += 1
    words += 1
    return words

def main():
    sentence = input("Give a sentence:\n")
    result = count_words(sentence)
    print(f"This sentence contains {result} words.")
main()   

