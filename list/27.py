salary = []

n = int(input("Enter number of employees: "))

for i in range(n):
    s = int(input("Enter salary: "))
    salary.append(s)

highest = max(salary)
lowest = min(salary)
average = sum(salary) / len(salary)

above = 0
below = 0

for s in salary:
    if s > 50000:
        above += 1
    if s < 30000:
        below += 1

print("Highest Salary =", highest)
print("Lowest Salary =", lowest)
print("Average Salary =", average)
print("Employees Above 50000 =", above)
print("Employees Below 30000 =", below)