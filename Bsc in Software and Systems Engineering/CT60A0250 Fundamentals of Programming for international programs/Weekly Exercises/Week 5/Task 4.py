stri = input("Give a string to compress:\n")
compressed = ""

str1 = stri.lower()
i = 0
length = len(str1)

while i < length:
    char = str1[i]
    count = 1

    while i + 1 < length and str1[i] == str1[i + 1]:
        count +=1
        i += 1

    if count > 1:
        compressed += char + str(count)
    else:
        compressed += char

    i += 1

compressed_ratio = round(len(compressed)/ len(stri), 2)

print(f"""Compressed string: {compressed}
Compressing ratio {compressed_ratio}""")

    
