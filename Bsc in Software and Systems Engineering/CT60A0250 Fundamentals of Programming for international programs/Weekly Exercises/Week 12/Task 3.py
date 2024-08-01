def reverse_string(S):
    if len(S) > 0:
        return reverse_string(S[1:]) + S[0]
    else: 
        return S
    
S = input("Give a string to reverse:\n")
print(f"Original String: {S}")
print(f"Reversed String: {reverse_string(S)}")