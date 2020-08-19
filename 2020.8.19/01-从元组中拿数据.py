"""
现有：``tuple1 = ("tom","kaisa","alisi","xiaoming","songshu")``
我想获得“alisi”这个内容，你能否想到三种方法来做？

#### 训练目标

元组按下标取值
元组的切片操作
元组的遍历操作
"""

tuple1 = ("tom", "kaisa", "alisi", "xiaoming", "songshu")

print(tuple1[2])
print(tuple1[2:3])

for str1 in tuple1:
    if str1 == 'alisi':
        print(str1)
