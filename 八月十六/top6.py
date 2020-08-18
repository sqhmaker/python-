'''
要求用户输入一个字符串，遍历当前字符串并打印，如果遇见“q”,则跳出循环。如果遇见“ ”（空格）则跳过当前输出。

#### 训练目标

- for循环的基本使用
- break的作用
- continue的作用
'''

str = input("输入一个字符串：")

for char in str:
    if char == "q":
        break
    elif char ==" ":
        continue
    print(char)
