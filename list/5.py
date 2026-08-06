students = ["Amit", "Rahul", "Sneha", "Priya", "Karan"]

print("Original List =", students)

students.pop(0)

students.pop()

name = input("Enter student name to remove: ")

if name in students:
    students.remove(name)
else:
    print("Student not found")

print("Remaining Students =", students)