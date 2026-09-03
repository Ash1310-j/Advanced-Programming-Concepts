# Program 1
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

file = open("student.txt", "w")
file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll_no + "\n")
file.write("Branch: " + branch + "\n")
file.write("Semester: " + semester + "\n")
file.close()

print("Student information written successfully.")


# Program 2
file = open("student.txt", "r")
data = file.read()
print("\nComplete contents of file:")
print(data)
file.close()


# Program 3
file = open("student.txt", "a")
file.write("Additional Information: Student of Computer Science\n")
file.close()

print("Additional information added successfully.")


# Program 4
file = open("student.txt", "r")
print("\nFile contents line by line:")
for line in file:
    print(line.strip())
file.close()


# Program 5
file = open("student.txt", "r")
lines = file.readlines()
print("\nTotal number of lines:", len(lines))
file.close()


# Program 6
file = open("student.txt", "r")
data = file.read()
words = data.split()
print("\nTotal number of words:", len(words))
file.close()


# Program 7
file = open("student.txt", "r")
data = file.read()
print("\nTotal number of characters:", len(data))
file.close()


# Program 8
file = open("student.txt", "r")
lines = file.readlines()

print("\nLines in reverse order:")
for line in reversed(lines):
    print(line.strip())
file.close()


# Program 9
file = open("student.txt", "r")
data = file.read()

vowels = 0
consonants = 0

for ch in data:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("\nNumber of vowels:", vowels)
print("Number of consonants:", consonants)
file.close()


# Program 10
file = open("student.txt", "r")
data = file.read()

alphabets = 0
digits = 0
spaces = 0
special = 0

for ch in data:
    if ch.isalpha():
        alphabets = alphabets + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch.isspace():
        spaces = spaces + 1
    else:
        special = special + 1

print("\nNumber of alphabets:", alphabets)
print("Number of digits:", digits)
print("Number of spaces:", spaces)
print("Number of special characters:", special)
file.close()

# Program 11
file = open("student.txt", "r")
data = file.read()
words = data.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
file.close()


# Program 12
file = open("student.txt", "r")
data = file.read()
words = data.split()

count = {}

for word in words:
    if word in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1

print("\nWord occurrences:")
print(count)
file.close()


# Program 13
search_word = input("\nEnter word to search: ")

file = open("student.txt", "r")
lines = file.readlines()

count = 0
line_numbers = []

for i in range(len(lines)):
    words = lines[i].split()

    for word in words:
        if word == search_word:
            count = count + 1
            line_numbers.append(i + 1)

print("Number of occurrences:", count)
print("Line numbers:", line_numbers)

file.close()


# Program 14
old_word = input("\nEnter word to replace: ")
new_word = input("Enter new word: ")

file = open("student.txt", "r")
data = file.read()
file.close()

data = data.replace(old_word, new_word)

file = open("student_new.txt", "w")
file.write(data)
file.close()

print("Word replaced successfully.")
print("Modified text is saved in student_new.txt")


# Program 15
file = open("program.py", "r")
lines = file.readlines()
file.close()

new_file = open("program_without_comments.py", "w")

for line in lines:
    if not line.strip().startswith("#"):
        new_file.write(line)

new_file.close()

print("\nSingle-line comments removed successfully.")

# Program 16
file = open("student.txt", "r")
data = file.read()
file.close()

file = open("uppercase.txt", "w")
file.write(data.upper())
file.close()

print("File converted to uppercase successfully.")


# Program 17
file = open("students.csv", "w")

file.write("RollNo,Name,Marks\n")
file.write("101,Amit,85\n")
file.write("102,Priya,92\n")
file.write("103,Rahul,78\n")

file.close()

file = open("students.csv", "r")
lines = file.readlines()
file.close()

print("\nAll student records:")

total = 0
highest = 0
highest_name = ""

for i in range(1, len(lines)):
    data = lines[i].strip().split(",")

    roll_no = data[0]
    name = data[1]
    marks = int(data[2])

    print(roll_no, name, marks)

    total = total + marks

    if marks > highest:
        highest = marks
        highest_name = name

print("\nStudent with highest marks:", highest_name)
print("Highest marks:", highest)

average = total / (len(lines) - 1)
print("Average marks:", average)

print("\nStudents who scored more than 80:")

for i in range(1, len(lines)):
    data = lines[i].strip().split(",")

    name = data[1]
    marks = int(data[2])

    if marks > 80:
        print(name, marks)


# Program 18

def display_employees():
    file = open("employees.txt", "r")
    print("\nAll employees:")

    for line in file:
        print(line.strip())

    file.close()


def highest_salary():
    file = open("employees.txt", "r")

    highest = 0
    highest_name = ""

    for line in file:
        data = line.strip().split(",")

        name = data[1]
        salary = int(data[3])

        if salary > highest:
            highest = salary
            highest_name = name

    file.close()

    print("\nHighest paid employee:", highest_name)
    print("Salary:", highest)


def average_salary():
    file = open("employees.txt", "r")

    total = 0
    count = 0

    for line in file:
        data = line.strip().split(",")

        salary = int(data[3])
        total = total + salary
        count = count + 1

    file.close()

    average = total / count
    print("Average salary:", average)


def above_salary(amount):
    file = open("employees.txt", "r")

    print("\nEmployees earning above", amount)

    for line in file:
        data = line.strip().split(",")

        name = data[1]
        salary = int(data[3])

        if salary > amount:
            print(name, salary)

    file.close()


file = open("employees.txt", "w")
file.write("1,Amit,IT,50000\n")
file.write("2,Priya,HR,60000\n")
file.write("3,Rahul,IT,45000\n")
file.write("4,Neha,Finance,70000\n")
file.close()

display_employees()
highest_salary()
average_salary()

salary = int(input("\nEnter salary: "))
above_salary(salary)


# Program 19
file = open("attendance.txt", "w")

file.write("Amit,80,100\n")
file.write("Priya,70,100\n")
file.write("Rahul,90,100\n")
file.write("Neha,65,100\n")

file.close()

file = open("attendance.txt", "r")

print("\nAttendance percentage:")

for line in file:
    data = line.strip().split(",")

    name = data[0]
    present = int(data[1])
    total = int(data[2])

    percentage = (present / total) * 100

    print(name, percentage, "%")

    if percentage < 75:
        print("Below 75%:", name)

file.close()


# Program 20
file = open("transactions.txt", "w")

file.write("D,5000\n")
file.write("W,1000\n")
file.write("D,3000\n")
file.write("W,500\n")
file.close()

file = open("transactions.txt", "r")

total_deposits = 0
total_withdrawals = 0
largest = 0
balance = 0

for line in file:
    data = line.strip().split(",")

    transaction = data[0]
    amount = int(data[1])

    if transaction == "D":
        total_deposits = total_deposits + amount
        balance = balance + amount
    else:
        total_withdrawals = total_withdrawals + amount
        balance = balance - amount

    if amount > largest:
        largest = amount

file.close()

print("\nTotal deposits:", total_deposits)
print("Total withdrawals:", total_withdrawals)
print("Final balance:", balance)
print("Largest transaction:", largest)

# Program 21

books = []

def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = [book_id, title, author, "Available"]
    books.append(book)

    print("Book added successfully.")


def search_book():
    book_id = input("Enter book ID to search: ")

    for book in books:
        if book[0] == book_id:
            print("Book ID:", book[0])
            print("Title:", book[1])
            print("Author:", book[2])
            print("Status:", book[3])
            return

    print("Book not found.")


def issue_book():
    book_id = input("Enter book ID to issue: ")

    for book in books:
        if book[0] == book_id:
            if book[3] == "Available":
                book[3] = "Issued"
                print("Book issued successfully.")
            else:
                print("Book is already issued.")
            return

    print("Book not found.")


def return_book():
    book_id = input("Enter book ID to return: ")

    for book in books:
        if book[0] == book_id:
            book[3] = "Available"
            print("Book returned successfully.")
            return

    print("Book not found.")


def display_available():
    print("\nAvailable books:")

    for book in books:
        if book[3] == "Available":
            print(book[0], book[1], book[2])


while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_book()

    elif choice == 2:
        search_book()

    elif choice == 3:
        issue_book()

    elif choice == 4:
        return_book()

    elif choice == 5:
        display_available()

    elif choice == 6:
        break

    else:
        print("Invalid choice.")


# Program 22

file1 = open("file1.txt", "r")
data1 = file1.read()
file1.close()

file2 = open("file2.txt", "r")
data2 = file2.read()
file2.close()

file3 = open("file3.txt", "w")
file3.write(data1)
file3.write("\n")
file3.write(data2)
file3.close()

print("Contents of both files copied into file3.txt")


# Program 23

file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

lines1 = file1.readlines()
lines2 = file2.readlines()

file1.close()
file2.close()

same = True

length = min(len(lines1), len(lines2))

for i in range(length):
    if lines1[i] != lines2[i]:
        print("Files are different.")
        print("First different line:", i + 1)
        print("File 1:", lines1[i].strip())
        print("File 2:", lines2[i].strip())
        same = False
        break

if same:
    if len(lines1) == len(lines2):
        print("Files are identical.")
    else:
        print("Files are different.")
        print("First different line:", length + 1)







