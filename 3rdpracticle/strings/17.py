s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")