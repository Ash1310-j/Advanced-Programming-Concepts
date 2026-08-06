temp = []

for i in range(30):
    t = float(input("Enter temperature: "))
    temp.append(t)

highest = max(temp)
lowest = min(temp)
average = sum(temp) / len(temp)

above = 0
below = 0

for t in temp:
    if t > average:
        above += 1
    elif t < average:
        below += 1

print("Hottest Day =", highest)
print("Coldest Day =", lowest)
print("Average Temperature =", average)
print("Days Above Average =", above)
print("Days Below Average =", below)