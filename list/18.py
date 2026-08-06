cart = ["Milk", "Bread", "Butter"]

item = input("Enter item to add: ")
cart.append(item)

item = input("Enter item to remove: ")

if item in cart:
    cart.remove(item)

item = input("Enter item to search: ")

if item in cart:
    print("Item Found")
else:
    print("Item Not Found")

print("Shopping Cart =", cart)
print("Total Items =", len(cart))