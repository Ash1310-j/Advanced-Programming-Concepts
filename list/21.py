list1 = []

n1 = int(input("Enter number of elements in first list: "))

for i in range(n1):
    num = int(input("Enter element: "))
    list1.append(num)

list2 = []

n2 = int(input("Enter number of elements in second list: "))

for i in range(n2):
    num = int(input("Enter element: "))
    list2.append(num)

merged = list1 + list2

print("Merged List =", merged)