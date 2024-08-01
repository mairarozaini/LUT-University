def occurences(ch, string):
    if len(ch) !=1:
        print("Error: Give a single character.")
        return -1

    count = 0

    for character in string:
        if character == ch:
            count +=1
    return count

def main():
    ch = input("Enter a character:\n")

    if len(ch) != 1:
        print("Error: Give a single character.")
        return

    string = input("Enter a string:\n")
    result = occurences(ch, string)

    if result != -1:
        print(f"The character '{ch}' appears {result} time(s) in the string.")

main()
