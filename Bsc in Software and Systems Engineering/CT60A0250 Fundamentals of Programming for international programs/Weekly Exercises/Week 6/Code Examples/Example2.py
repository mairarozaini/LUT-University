initial_list = [1, 2, 3]

def mystery(L):
    if len(L) >= 1:
        L[0] = "?"

print("Before:", initial_list)
mystery(initial_list)
print("After:", initial_list)
