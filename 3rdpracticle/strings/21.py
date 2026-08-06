password = input("Enter Password: ")

upper = 0
lower = 0
digit = 0
special = 0

for ch in password:
    if ch.isupper():
        upper = upper + 1
    elif ch.islower():
        lower = lower + 1
    elif ch.isdigit():
        digit = digit + 1
    else:
        special = special + 1

if len(password) >= 8 and upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
    print("Valid Password")
else:
    print("Invalid Password")