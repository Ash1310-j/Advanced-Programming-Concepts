numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

reverse_list = []

for i in range(len(numbers) - 1, -1, -1):
    reverse_list.append(numbers[i])

print("Original List =", numbers)
print("Reversed List =", reverse_list)