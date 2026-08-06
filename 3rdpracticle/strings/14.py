s = input("Enter a sentence: ")

words = s.split()

result = ""

for word in words:
    result = result + word.capitalize() + " "

print("Title Case =", result)