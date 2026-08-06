a = []
b = []
c = []

print("Enter First Matrix")

for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input()))
    a.append(row)

print("Enter Second Matrix")

for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input()))
    b.append(row)

for i in range(3):
    row = []
    for j in range(3):
        row.append(a[i][j] + b[i][j])
    c.append(row)

print("Result Matrix")

for row in c:
    print(row)