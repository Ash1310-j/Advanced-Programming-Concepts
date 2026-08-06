books = ["Python", "Java", "C", "DBMS"]

book = input("Enter book to add: ")
books.append(book)

book = input("Enter book to search: ")

if book in books:
    print("Book Found")
else:
    print("Book Not Found")

book = input("Enter book to remove: ")

if book in books:
    books.remove(book)

print("Book List =", books)
print("Total Books =", len(books))