s = input("Enter a paragraph: ")

words = s.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] = freq[word] + 1
    else:
        freq[word] = 1

for word in freq:
    print(word, "=", freq[word])