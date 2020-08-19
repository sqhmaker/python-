"""
现有列表：
``name_list =["tom","kaisa","alisi",["xiaoming","songshu"]]``
现在有个要求，将最外层的列表转换成元组存储，里面的小列表不变；
并且向小列表中添加一个元素“python”

#### 训练目标

1. 元组的强制转换
2. 元组虽然是不可变类型，但是元组中的列表是可变的
"""

name_list = ["tom", "kaisa", "alisi", ["xiaoming", "songshu"]]
tuple1 = tuple(name_list)
print(tuple1)

tuple1[-1].append('python')
print(tuple1)