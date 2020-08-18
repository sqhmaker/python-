'''
将下列两个列表合并，将合并后的列表去重，之后降序并输出

list1 = [11, 45, 34, 51, 90]
list2 = [4, 16, 23, 0]

#### 训练目标

列表操作方法的使用
'''
list1 = [11, 45, 34, 51, 90]
list2 = [4, 16, 23, 0, 11, 100]

list3 = list2 + list1
list4 = list(set(list3))
list4.sort(reverse=True)
print(list4)