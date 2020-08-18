'''
使用for循环计算从0到用户输入的值的累加和

#### 训练目标

range()的使用
'''


number = int(input("输入一个数字："))
sum = 0
for i in range(number + 1):
    sum += i

print(sum)