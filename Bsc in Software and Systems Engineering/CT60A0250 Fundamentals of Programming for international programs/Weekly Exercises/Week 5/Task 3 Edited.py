def occurences(ch, string):
    count = 0

    for character in string:
        if character == ch:
            count +=1
    return count

def anagram(A,B):
    if len(A) != len(B):
        return False

    for character in A:
        if occurences(character, A) != occurences(character, B):
            return False

    return True


def main():
    A = input("Enter string A:\n")
    B = input("Enter string B:\n")

    result = anagram(A,B)

    if result:
        print(f"{A} and {B} are anagrams")
    else:
        print(f"{A} and {B} are not anagrams")
main()
