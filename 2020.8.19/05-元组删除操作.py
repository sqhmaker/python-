"""
现有字典``dict1 = {'name':'chuanzhi','age':18}``
  要求：

​	1.删除age：18这个键值对

​	2.将整个字典里面的所有键值对，清空

#### 训练目标

1. 对于字典中删除的操作
2. del的使用
3. clear() 的使用
"""
dict1 = {'name':'chuanzhi','age':18}
print(dict1)
del dict1['age']
print(dict1)
dict1.clear()
print(dict1)