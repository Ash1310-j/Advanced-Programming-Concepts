text = input("Enter Message: ")
shift = int(input("Enter Shift Value: "))

result = ""

for ch in text:
    if ch.isalpha():
        new = chr(ord(ch) + shift)
        result = result + new
    else:
        result = result + ch

print("Encrypted Message =", result)

text = input("Enter Encrypted Message: ")
shift = int(input("Enter Shift Value: "))

result = ""

for ch in text:
    if ch.isalpha():
        new = chr(ord(ch) - shift)
        result = result + new
    else:
        result = result + ch

print("Original Message =", result)