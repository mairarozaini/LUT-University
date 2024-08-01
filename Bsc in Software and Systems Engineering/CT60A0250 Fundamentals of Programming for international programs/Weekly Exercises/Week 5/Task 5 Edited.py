def substring(first_string, sec_string):
    length1 = len(first_string)
    length2 = len(sec_string)

    for words in range(length2 - length1 + 1):
        found = True

        for ch in range(length1):
            if sec_string[words + ch] != first_string[ch]:
                found = False
                break
            
        if found:
            return True

    return False

def main():
    first_string = input("Enter the first string:\n")
    sec_string = input("Enter the second string:\n")

    if substring(first_string, sec_string) == True:
        print("The first string can be found in the second string.")
    else:
        print("The first string cannot be found in the second string.")
main()
