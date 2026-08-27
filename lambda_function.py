# Problem 1
square = lambda n: n * n

n = int(input("Enter a number: "))
print("Square =", square(n))

# Problem 2
cube = lambda n: n * n * n

n = int(input("Enter a number: "))
print("Cube =", cube(n))

# Problem 3
even_odd = lambda n: n % 2 == 0

n = int(input("Enter a number: "))
print(even_odd(n))


# Problem 4
maximum = lambda a, b: a if a > b else b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Maximum =", maximum(a, b))


# Problem 5
simple_interest = lambda p, r, t: (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
print("Simple Interest =", simple_interest(p, r, t))

# Problem 6
numbers = list(map(int, input("Enter numbers: ").split()))
squares = list(map(lambda n: n * n, numbers))

print("Squares =", squares)


# Problem 7
numbers = list(map(int, input("Enter numbers: ").split()))
cubes = list(map(lambda n: n * n * n, numbers))

print("Cubes =", cubes)


# Problem 8
numbers1 = list(map(int, input("Enter first list: ").split()))
numbers2 = list(map(int, input("Enter second list: ").split()))

result = list(map(lambda a, b: a + b, numbers1, numbers2))

print("Sum =", result)
# Problem 41
numbers = list(map(int, input("Enter numbers: ").split()))
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))

print("Even numbers =", even_numbers)


# Problem 9
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

numbers = list(map(int, input("Enter numbers: ").split()))
prime_numbers = list(filter(lambda n: is_prime(n), numbers))

print("Prime numbers =", prime_numbers)


# Problem 10
numbers = list(map(int, input("Enter numbers: ").split()))
positive_numbers = list(filter(lambda n: n > 0, numbers))

print("Positive numbers =", positive_numbers)


# Problem 11
numbers = list(map(int, input("Enter numbers: ").split()))
greater_numbers = list(filter(lambda n: n > 50, numbers))

print("Numbers greater than 50 =", greater_numbers)


# Problem 12
words = input("Enter words: ").split()
long_words = list(filter(lambda word: len(word) > 5, words))

print("Words having more than five characters =", long_words)


# Problem 13
words = input("Enter words: ").split()
words.sort(key=lambda word: len(word))

print("Sorted words =", words)


# Problem 14
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students.append((name, marks))

students.sort(key=lambda student: student[1])

print("Students sorted according to marks:")
for student in students:
    print(student)


# Problem 15
employees = []

n = int(input("Enter number of employees: "))

for i in range(n):
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    employees.append((name, salary))

employees.sort(key=lambda employee: employee[1])

print("Employees sorted according to salary:")
for employee in employees:
    print(employee)


# Problem 16
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students.append((name, marks))

total = sum(map(lambda student: student[1], students))
avg = total / len(students)

above_75 = list(filter(lambda student: student[1] > 75, students))
students.sort(key=lambda student: student[1])

print("Average marks =", avg)
print("Students scoring above 75 =", above_75)
print("Students sorted according to marks =", students)


# Problem 17
employees = []

n = int(input("Enter number of employees: "))

for i in range(n):
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))
    employees.append((name, department, salary))

high_salary = list(filter(lambda employee: employee[2] > 50000, employees))

increased_salary = list(
    map(lambda employee: (employee[0], employee[1], employee[2] * 1.10), employees)
)

employees.sort(key=lambda employee: employee[2])

print("Employees earning more than 50000 =", high_salary)
print("Salaries after 10% increase =", increased_salary)
print("Employees sorted according to salary =", employees)


# Problem 18
products = []

n = int(input("Enter number of products: "))

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    products.append((name, price, quantity))

total_values = list(
    map(lambda product: (product[0], product[1] * product[2]), products)
)

costly_products = list(
    filter(lambda product: product[1] * product[2] > 1000, products)
)

products.sort(key=lambda product: product[1] * product[2])

print("Total value of each product =", total_values)
print("Products costing more than 1000 =", costly_products)
print("Products sorted according to total value =", products)

# Problem 19
words = input("Enter words: ").split()

lengths = list(map(lambda word: len(word), words))
long_words = list(filter(lambda word: len(word) > 5, words))
sorted_words = sorted(words, key=lambda word: len(word))

print("Length of every word =", lengths)
print("Words having more than five characters =", long_words)
print("Words sorted according to length =", sorted_words)



