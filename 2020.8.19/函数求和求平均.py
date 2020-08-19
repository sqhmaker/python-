'''
1. 写一个函数求三个数的和
2. 写一个函数求三个数的平均值
'''


def sum3(a, b, c):
    sum_number = a + b + c
    return sum_number


def average3(a, b, c):
    average_number = sum3(a, b, c) / 3
    return average_number


result1 = sum3(1, 2, 3)
result2 = average3(1, 2, 3)
print(result1)
print(result2)
