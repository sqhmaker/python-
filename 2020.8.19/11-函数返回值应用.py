"""
 定义一个函数 sum_random 接收二个参数 m, n ，在函数中计算 m + n 的值，并打印结果，要求 m 和 n 是 1 -- 100 之间的数
  第一步：定义函数并接收两个参数

  第二步：判断这两个参数是都在1-100之间，如果在，将这两个数相加值保存，如果不在则提示输入错误

  第三步：调用函数
"""


def sum_random(m, n):
    if 1 <= m <= 100 and 1 <= n <= 100:
        return m + n
    else:
        # print('输入不符合要求，要求 m 和 n 是 1 -- 100 之间的数')
        return '输入不符合要求，要求 m 和 n 是 1 -- 100 之间的数'


num1 = int(input('enter first number:'))
num2 = int(input('enter second number:'))
result = sum_random(num2, num1)
print(result)
