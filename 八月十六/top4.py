'''
设计“过7游戏”的程序, 打印出1-100之间除了7和7的倍数之外的所有数字，如果遇见7和7的倍数则打印“哈~”跳过本次循环。

#### 训练目标

- while中的continue的使用
思路
首先 while 循环1到100

'''
# i = 1
# while i <= 100:
#     if i % 7 == 0:
#         print("哈~")
#     else:
#         print(i)
#     i += 1
#
i = 0
while i <= 100:
    i += 1
    if i % 7 == 0:
        print("哈~")
        continue
    print(i)

