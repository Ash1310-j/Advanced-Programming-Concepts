s1 = input("Enter First String: ")
s2 = input("Enter Second String: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes, It is Rotation")
else:
    print("No, It is Not Rotation")