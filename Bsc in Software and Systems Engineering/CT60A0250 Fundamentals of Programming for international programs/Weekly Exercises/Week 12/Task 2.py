def power(x, n):
    if n > 0:
        return x * power(x, n-1)
    else:
        return 1

x = float(input("Give a float x:\n"))
n = int(input("Give a non-negative integer n:\n"))
print(f"{x} power to {n} is {power(x,n)}")