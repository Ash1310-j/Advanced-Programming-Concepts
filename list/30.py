patients = ["Rahul", "Amit", "Sneha"]
ages = [30, 45, 25]

name = input("Enter patient name to add: ")
age = int(input("Enter age: "))

patients.append(name)
ages.append(age)

delete = input("Enter patient name to delete: ")

if delete in patients:
    index = patients.index(delete)
    patients.pop(index)
    ages.pop(index)

search = input("Enter patient name to search: ")

if search in patients:
    print("Patient Found")
else:
    print("Patient Not Found")

print("Patient Records")

for i in range(len(patients)):
    print(patients[i], "-", ages[i])

print("Total Patients =", len(patients))