A = input("Enter string A:\n")
B = input("Enter string B:\n")

A1 = A.lower()
B2 = B.lower()

A2 = list(A)
B2 = list(B)

anagram_A = A2.sort()
anagram_B = B2.sort()

if (len(A) == len(B)) and (anagram_A == anagram_B):
    print(f"{A} and {B} are anagrams")

else:
    print(f"{A} and {B} are not anagrams")
    
