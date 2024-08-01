number_list = []
while True:
    new_number = input("Enter an integer (or 'done' to finish):\n")
    try:
        number_list.append(int(new_number))
    except ValueError:
        if new_number == 'done':
            break

target = int(input("Enter the target sum:\n"))
pairs = []

for i in range(0, len(number_list)):
    for j in range(0, len(number_list)):
        if number_list[i] + number_list[j] == target:
            pairs.append((number_list[i], number_list[j]))

print(f"Pairs with a sum of {target}:")
for x in pairs:
    print(x)