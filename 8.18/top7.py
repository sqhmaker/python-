'''
给定一个列表，首先删除以s开头的元素，删除后，修改第一个元素为"joke"，并且并且把最后一个元素复制一份，放在joke的后边

my_list = ["spring", "look", "strange", "curious", "black", "hope"]

#### 训练目标

 列表包含的操作
 列表的相关操作
'''
my_list = ["spring", "look", "strange", "curious", "black", "hope"]
for word in my_list:
    if word.startswith('s') :
        my_list.remove(word)
print(my_list)
my_list[0] = 'joke'
my_list.insert(1,my_list[-1])
print(my_list)