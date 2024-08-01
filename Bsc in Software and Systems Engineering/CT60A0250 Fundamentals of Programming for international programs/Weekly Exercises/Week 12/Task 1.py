def integer_sum(n):
    if n - 2 > 1:
        return n + integer_sum(n-2)
    else:
        return n
    
n = int(input("Give a non-negative integer n:\n"))
print(f"n + (n-2) + (n-4) + ... = {integer_sum(n)}")