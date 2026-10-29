def calculate_performance():
    marks_list = []
    print("enter marks for 5 subjects:")
    for i in range(1, 6):
        marks = float(input(f"Enter marks for Subject {i}: "))
        marks_list.append(marks)
    total = sum(marks_list)
    percentage = (total / 500) * 100   

    print("Student Performance Report")
    print("Total Marks Scored:", total, "/ 500")
    print("Overall Percentage:", percentage, "%")
calculate_performance()
