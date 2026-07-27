from functools import reduce

def sum_all(num1, num2):
    return num1 + num2

numbers = [1,24,45,12,3]

result = reduce(sum_all, numbers)

print(result)