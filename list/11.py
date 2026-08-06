numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

print("First 5 Elements =", numbers[:5])
print("Last 5 Elements =", numbers[-5:])
print("Middle 4 Elements =", numbers[3:7])
print("Alternate Elements =", numbers[::2])
print("Reverse List =", numbers[::-1])