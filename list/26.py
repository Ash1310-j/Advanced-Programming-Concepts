marks = []

for i in range(20):
    mark = int(input("Enter marks: "))
    marks.append(mark)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above = 0
below = 0

for mark in marks:
    if mark > average:
        above += 1
    elif mark < average:
        below += 1

print("Highest Marks =", highest)
print("Lowest Marks =", lowest)
print("Average Marks =", average)
print("Students Above Average =", above)
print("Students Below Average =", below)