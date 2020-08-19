"""
现有字典``dict1 = {'name':'chuanzhi','age':18}``
要求：

​	1.使用循环将字典中所有的键输出到屏幕上
​    2.使用循环将字典中所有的键输出到屏幕上
​    3.使用循环将字典中所有的键值对输出到屏幕上
​      输出方式：

​				name：chuanzhi
​                 age:18

#### 训练目标

1. for循环的使用复习
2. 学会如何获取字典所有的键
3. 学会如何获取字典所有的值
4. 学会如何获取字典所有的键值对
"""
dict1 = {'name': 'chuanzhi', 'age': 18}

for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

for key, value in dict1.items():
    # print(f"{key}:{value}")
    print(key, ':', value)
