def avg_numbers(a, b, c):
    import math
    average = ((a + b + c)/3)
    return average

numbers = 3, 6, 7
print("The averge is :",avg_numbers(*numbers))
