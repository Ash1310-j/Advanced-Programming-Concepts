def count_elements(numbers):   
    counts = {
        "even": 0,
        "odd": 0,
        "positive": 0,
        "negative": 0
    } 
    for num in numbers:
  
        if num > 0:
            counts["positive"] += 1
        elif num < 0:
            counts["negative"] += 1
        if num % 2 == 0:
            counts["even"] += 1
        else:
            counts["odd"] += 1       
    return counts
list = [1, -2, 3, -4, 5, 0, 11, -15]
print(count_elements(list))

