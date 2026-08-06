numbers = [10, 20, 30, 40]

print("Original List =", numbers)

end = int(input("Enter element to add at end: "))
numbers.append(end)

begin = int(input("Enter element to add at beginning: "))
numbers.insert(0, begin)

pos = int(input("Enter position: "))
value = int(input("Enter value: "))
numbers.insert(pos, value)

print("Updated List =", numbers)