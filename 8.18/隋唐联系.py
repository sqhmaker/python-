'''
5. 给定字符串 "abcdefghi"，使用切片取出 下标 0-4 的字符。
6. 根据课件练习字符串常见操作的方法。
7. 定义一个列表，列表中的元素有 ``张三、李四、王五、赵六``
8. 分别使用for循环和while循环打印出 练习7 列表中的元素
9. 向练习7的列表中追加一个名字 ``小明``
10. 将 练习7 列表中名字``李四`` 改为 ``赵四``
11. 将练习7 列表中的 ``赵六`` 删除
12. 给定一个列表 ``[32, 17, 28, 90, 11]`` 完成对该列表的升序和降序的排序
'''


list1 = ['张三','李四','王五','赵六']
for name in list1:
    print(name)
i = 0
while i <len(list1):
    print(list1[i])
    i += 1
list1.append('小明')
list1[1] = '赵四'
list1.remove('赵六')
print(list1)
list2 = [32, 17, 28, 90, 11]
print(list(set(list2)))
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)

'''
str1 = "abcdefghi"
print(str1[0:5:1])
print(str1.index("fg"))
print(str1.split('c'))
print(str1.join("d"))
print(str1.replace('f','er'))
print(str1.count('a'))

'''