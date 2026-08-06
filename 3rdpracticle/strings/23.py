s = input("Enter a string: ")

result = ""
count = 1

for i in range(len(s)):
    if i < len(s) - 1 and s[i] == s[i + 1]:
        count = count + 1
    else:
        result = result + s[i] + str(count)
        count = 1

if len(result) < len(s):
    print("Compressed String =", result)
else:
    print("Original String =", s)