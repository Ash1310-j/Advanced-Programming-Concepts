
# Program 1: Create a tuple of five integers and display it
numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)

# Program 2: Create a tuple of five city names and display
# first, last and third city
cities = ("Pune", "Mumbai", "Delhi", "Nagpur", "Nashik")

print("First city:", cities[0])
print("Last city:", cities[-1])
print("Third city:", cities[2])

# Program 3: Create a tuple of student names and display
# total number of students
students = ("Amit", "Sneha", "Rahul", "Priya", "Neha")

print("Total students:", len(students))

# Program 4: Check whether a given color exists in the tuple
colors = ("Red", "Blue", "Green", "Yellow", "Black")

color = input("Enter a color: ")

if color in colors:
    print("Color exists in the tuple")
else:
    print("Color does not exist in the tuple")


# Program 5: Create a tuple of fruits and display each fruit
# using a loop
fruits = ("Apple", "Mango", "Banana", "Orange", "Grapes")

for fruit in fruits:
    print(fruit)


# Program 6: Count how many times a particular number appears
numbers = (10, 20, 10, 30, 10, 40, 20, 10)

number = int(input("Enter number to count: "))

print("Number of times it appears:", numbers.count(number))


# Program 7: Find the index of a given employee ID
employee_ids = (101, 102, 103, 104, 105)

employee_id = int(input("Enter employee ID: "))

if employee_id in employee_ids:
    print("Index:", employee_ids.index(employee_id))
else:
    print("Employee ID not found")


# Program 8: Concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print("Concatenated tuple:", result)

# Program 9: Repeat a tuple four times
numbers = (1, 2, 3)

result = numbers * 4

print("Repeated tuple:", result)


# Program 10: Perform different slicing operations
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("First five elements:", numbers[:5])
print("Last five elements:", numbers[5:])
print("Middle four elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse tuple:", numbers[::-1])

# Program 11: Convert tuple into list and add a new element
numbers = (10, 20, 30, 40)

number_list = list(numbers)
number_list.append(50)

print("List after adding element:", number_list)


# Program 12: Accept five numbers, store in list and convert
# the list into a tuple
number_list = []

for i in range(5):
    number = int(input("Enter number: "))
    number_list.append(number)

number_tuple = tuple(number_list)

print("Tuple:", number_tuple)


# Program 13: Modify a tuple by converting it into a list
# and then back into a tuple
numbers = (10, 20, 30, 40)

number_list = list(numbers)

number_list[1] = 25

numbers = tuple(number_list)

print("Modified tuple:", numbers)


# Program 14: Create a tuple and delete it completely
numbers = (10, 20, 30, 40)

del numbers

print("Tuple deleted successfully")


# Program 15: Create a nested tuple containing student details
# and display each record
students = (
    (1, "Amit", "Computer Science"),
    (2, "Sneha", "Information Technology"),
    (3, "Rahul", "Computer Science")
)

for student in students:
    print(student)


# Program 16: Store ten numbers in a tuple and calculate sum
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

total = 0

for number in numbers:
    total = total + number

print("Sum:", total)


# Program 17: Find largest and smallest number without using
# max() and min()
numbers = (25, 10, 45, 5, 30, 60, 15)

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("Largest number:", largest)
print("Smallest number:", smallest)


# Program 18: Calculate average of elements in a tuple
numbers = (10, 20, 30, 40, 50)

total = 0

for number in numbers:
    total = total + number

average = total / len(numbers)

print("Average:", average)


# Program 19: Count even and odd numbers in a tuple
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)


# Program 20: Check whether a user-given number exists
# in the tuple
numbers = (10, 20, 30, 40, 50)

number = int(input("Enter number: "))

if number in numbers:
    print("Number exists in the tuple")
else:
    print("Number does not exist in the tuple")


# Program 21: Store and display student details
# Roll Number, Name, Department and Marks
student = (101, "Ashwini", "Computer Science", 85)

print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])


# Program 22: Store employee ID, name and salary
# and display employee information
employees = (
    (101, "Amit", 30000),
    (102, "Sneha", 35000),
    (103, "Rahul", 40000)
)

for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print()


# Program 23: Calculate total bill, average price,
# highest-priced item and lowest-priced item
prices = (100, 250, 150, 500, 300)

total_bill = sum(prices)
average_price = total_bill / len(prices)
highest_price = max(prices)
lowest_price = min(prices)

print("Total bill:", total_bill)
print("Average price:", average_price)
print("Highest price:", highest_price)
print("Lowest price:", lowest_price)


# Program 24: Store temperatures of seven days and determine
# maximum, minimum and average temperature
temperatures = (32, 35, 31, 30, 34, 36, 33)

total = sum(temperatures)
average = total / len(temperatures)

print("Maximum temperature:", max(temperatures))
print("Minimum temperature:", min(temperatures))
print("Average temperature:", average)


# Program 25: Store runs scored in 10 matches and calculate
# total, highest, lowest and average score
runs = (45, 67, 23, 89, 56, 34, 78, 91, 50, 62)

total_runs = sum(runs)
highest_score = max(runs)
lowest_score = min(runs)
average_score = total_runs / len(runs)

print("Total runs:", total_runs)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)
print("Average score:", average_score)


# Program 26: Find common elements between two tuples
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

common = ()

for number in tuple1:
    if number in tuple2:
        common = common + (number,)

print("Common elements:", common)


# Program 27: Merge two tuples and remove duplicate elements
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)

merged = tuple1 + tuple2

result = ()

for number in merged:
    if number not in result:
        result = result + (number,)

print("Tuple after removing duplicates:", result)


# Program 28: Count the frequency of each element in a tuple
numbers = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print("Frequency of each element:")

for number in frequency:
    print(number, ":", frequency[number])


# Program 29: Convert tuple into sorted tuple in ascending
# and descending order
numbers = (50, 20, 40, 10, 30)

ascending = tuple(sorted(numbers))
descending = tuple(sorted(numbers, reverse=True))

print("Ascending order:", ascending)
print("Descending order:", descending)


# Program 30: Patient records
# Display all records, search by ID, count patients and
# display patients with a specific blood group
patients = (
    (101, "Amit", 25, "A+"),
    (102, "Sneha", 30, "B+"),
    (103, "Rahul", 28, "O+"),
    (104, "Priya", 22, "A+"),
    (105, "Neha", 35, "O-")
)

print("All Patient Records:")

for patient in patients:
    print(patient)

patient_id = int(input("Enter patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == patient_id:
        print("Patient found:")
        print("Patient ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Blood Group:", patient[3])
        found = True
        break

if not found:
    print("Patient not found")

print("Total patients:", len(patients))
blood_group = input("Enter blood group: ")

print("Patients with blood group", blood_group, ":")

for patient in patients:
    if patient[3] == blood_group:
        print(patient)