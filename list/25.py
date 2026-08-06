numbers = [10, 20, 10, 30, 20, 40, 50, 30]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List After Removing Duplicates =", unique)