numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Elements at Even Index:")

for i in range(0, len(numbers), 2):
    print(numbers[i])