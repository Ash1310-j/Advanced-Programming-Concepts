# Problem 1
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

n = int(input("Enter a number: "))
print("Factorial =", factorial(n))


# Problem 2
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter a number: "))
print(check_even_odd(n))


# Problem 3
def greater(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Greater number =", greater(a, b))


# Problem 4
def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
print("Simple Interest =", simple_interest(p, r, t))


# Problem 5
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
print(is_prime(n))


# Problem 6
def circle_area(r):
    return 3.14 * r * r

r = float(input("Enter radius: "))
print("Area of circle =", circle_area(r))


# Problem 7
def natural_sum(n):
    return n * (n + 1) // 2

n = int(input("Enter n: "))
print("Sum =", natural_sum(n))


# Problem 8
def power(base, exponent):
    result = 1
    for i in range(exponent):
        result = result * base
    return result

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print("Answer =", power(base, exponent))


# Problem 9
def largest(numbers):
    large = numbers[0]
    for n in numbers:
        if n > large:
            large = n
    return large

numbers = list(map(int, input("Enter numbers: ").split()))
print("Largest =", largest(numbers))


# Problem 10
def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

s = input("Enter a string: ")
print("Number of vowels =", count_vowels(s))


# Problem 11
def reverse_string(s):
    return s[::-1]

s = input("Enter a string: ")
print("Reverse =", reverse_string(s))


# Problem 12
def palindrome(value):
    value = str(value)
    return value == value[::-1]

value = input("Enter a string or number: ")
print(palindrome(value))


# Problem 13
def average(numbers):
    return sum(numbers) / len(numbers)

numbers = list(map(int, input("Enter numbers: ").split()))
print("Average =", average(numbers))


# Problem 14
def count_element(numbers, element):
    count = 0
    for n in numbers:
        if n == element:
            count += 1
    return count

numbers = list(map(int, input("Enter numbers: ").split()))
element = int(input("Enter element: "))
print("Occurrences =", count_element(numbers, element))


# Problem 15
def unique_elements(numbers):
    result = []
    for n in numbers:
        if n not in result:
            result.append(n)
    return result

numbers = list(map(int, input("Enter numbers: ").split()))
print("Unique elements =", unique_elements(numbers))


# Problem 16
def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()
    return unique[-2]

numbers = list(map(int, input("Enter numbers: ").split()))
print("Second largest =", second_largest(numbers))


# Problem 17
def fibonacci(n):
    result = []
    a = 0
    b = 1

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result

n = int(input("Enter n: "))
print("Fibonacci numbers =", fibonacci(n))


# Problem 18
def student_result(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade

marks = []
for i in range(5):
    marks.append(float(input("Enter marks: ")))

percentage, grade = student_result(marks[0], marks[1], marks[2], marks[3], marks[4])
print("Percentage =", percentage)
print("Grade =", grade)


# Problem 19
def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

    return bill

units = int(input("Enter units consumed: "))
print("Electricity Bill =", electricity_bill(units))


# Problem 20
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    return basic + hra + da

basic = float(input("Enter basic salary: "))
print("Gross Salary =", gross_salary(basic))


# Problem 21
def total_bill(prices, quantities, discount):
    total = 0

    for i in range(len(prices)):
        total = total + prices[i] * quantities[i]

    total = total - (total * discount / 100)
    return total

prices = list(map(float, input("Enter prices: ").split()))
quantities = list(map(int, input("Enter quantities: ").split()))
discount = float(input("Enter discount percentage: "))

print("Total Bill =", total_bill(prices, quantities, discount))


# Problem 22
def number_details(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    
    for n in numbers:
        if n < minimum:
            minimum = n
        if n > maximum:
            maximum = n

    total = sum(numbers)
    avg = total / len(numbers)

    return minimum, maximum, total, avg

numbers = list(map(int, input("Enter numbers: ").split()))
minimum, maximum, total, avg = number_details(numbers)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Sum =", total)
print("Average =", avg)


# Problem 23
def student_total(marks):
    return sum(marks)

def student_percentage(marks):
    return sum(marks) / 5

def student_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = list(map(float, input("Enter marks of 5 subjects: ").split()))

    total = student_total(marks)
    percentage = student_percentage(marks)
    grade = student_grade(percentage)

    students.append({
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    })

class_total = 0

for student in students:
    print(student["name"], student["roll"], student["total"], student["percentage"], student["grade"])
    class_total += student["percentage"]

class_average = class_total / n
highest = students[0]
lowest = students[0]

for student in students:
    if student["percentage"] > highest["percentage"]:
        highest = student
    if student["percentage"] < lowest["percentage"]:
        lowest = student

print("Class Average =", class_average)
print("Highest Scorer =", highest["name"])
print("Lowest Scorer =", lowest["name"])


# Problem 24
balance = 0
transactions = []

def deposit(amount):
    global balance
    balance += amount
    transactions.append("Deposited " + str(amount))

def withdrawal(amount):
    global balance

    if amount <= balance:
        balance -= amount
        transactions.append("Withdrawn " + str(amount))
        return True
    else:
        return False

def balance_enquiry():
    return balance

def transaction_history():
    return transactions

deposit(5000)
print("Balance =", balance_enquiry())

amount = float(input("Enter withdrawal amount: "))

if withdrawal(amount):
    print("Withdrawal successful")
else:
    print("Insufficient balance")

print("Balance =", balance_enquiry())
print("Transactions =", transaction_history())


# Problem 25
books = {}

def add_book(book_id, name):
    books[book_id] = {"name": name, "available": True}

def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        return "Book issued"
    return "Book not available"

def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        return "Book returned"
    return "Book not found"

def search_book(book_id):
    if book_id in books:
        return books[book_id]
    return "Book not found"

def display_books():
    for book_id, book in books.items():
        if book["available"]:
            print(book_id, book["name"])

add_book(1, "Python")
add_book(2, "Java")
add_book(3, "C++")

print("Available books:")
display_books()

print(issue_book(1))

print("Available books:")
display_books()

print(return_book(1))


# Problem 26
def calculate_units_charge(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 100 * 5 + (units - 100) * 7
    else:
        return 100 * 5 + 100 * 7 + (units - 200) * 10

def fixed_charge():
    return 100

def calculate_tax(amount):
    return amount * 0.05

def calculate_discount(amount):
    if amount > 5000:
        return amount * 0.10
    return 0

def final_electricity_bill(units):
    charge = calculate_units_charge(units)
    fixed = fixed_charge()
    tax = calculate_tax(charge)
    discount = calculate_discount(charge)

    return charge + fixed + tax - discount

units = int(input("Enter units consumed: "))
print("Final Electricity Bill =", final_electricity_bill(units))


# Problem 27
def consultation_charges():
    return 500

def laboratory_charges():
    return 1000

def medicine_charges():
    return 1500

def room_charges(days):
    return days * 1000

def final_hospital_bill(category, days):
    total = consultation_charges() + laboratory_charges() + medicine_charges() + room_charges(days)

    if category.lower() == "senior":
        total = total * 0.90
    elif category.lower() == "child":
        total = total * 0.95

    return total

category = input("Enter patient category: ")
days = int(input("Enter number of room days: "))

print("Final Bill =", final_hospital_bill(category, days))


# Problem 28
products = {}

def add_product(name, price, quantity):
    products[name] = [price, quantity]

def remove_product(name):
    if name in products:
        del products[name]

def calculate_subtotal():
    total = 0

    for product in products.values():
        total += product[0] * product[1]

    return total

def coupon_discount(total):
    if total >= 5000:
        return total * 0.10
    return 0

def calculate_gst(amount):
    return amount * 0.18

def final_invoice():
    subtotal = calculate_subtotal()
    discount = coupon_discount(subtotal)
    amount = subtotal - discount
    gst = calculate_gst(amount)

    return subtotal, discount, gst, amount + gst

add_product("Laptop", 50000, 1)
add_product("Mouse", 1000, 2)

subtotal, discount, gst, final = final_invoice()

print("Subtotal =", subtotal)
print("Discount =", discount)
print("GST =", gst)
print("Final Amount =", final)


# Problem 29
def binary_search(numbers, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] == target:
        return mid
    elif target < numbers[mid]:
        return binary_search(numbers, target, low, mid - 1)
    else:
        return binary_search(numbers, target, mid + 1, high)

numbers = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter element to search: "))

result = binary_search(numbers, target, 0, len(numbers) - 1)

if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)


# Problem 30
def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)

n = int(input("Enter decimal number: "))

if n == 0:
    print("Binary = 0")
else:
    print("Binary =", decimal_to_binary(n))


# Problem 31
def recursive_palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return recursive_palindrome(s[1:-1])

s = input("Enter a string: ")

if recursive_palindrome(s):
    print("Palindrome")
else:
    print("Not palindrome")


# Problem 32
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"

def calculate(a, b, operation):
    return operation(a, b)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", calculate(a, b, addition))
print("Subtraction =", calculate(a, b, subtraction))
print("Multiplication =", calculate(a, b, multiplication))
print("Division =", calculate(a, b, division))