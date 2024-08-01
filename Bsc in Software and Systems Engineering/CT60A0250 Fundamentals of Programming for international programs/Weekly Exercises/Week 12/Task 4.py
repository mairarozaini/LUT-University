def gcd(a,b):
    if b > 0:
        return gcd(b, a % b)
    else:
        return a
    
numbers = input("Give two positive integers separated by comma:\n")
a, b = map(int, numbers.split(','))

print(f"gcd({a},{b}) = {gcd(a, b)}")