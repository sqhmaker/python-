'''
有一个列表，判断列表中的每一个元素是否以s或e结尾，如果是，则将其放入一个新的列表中，最后输出这个新的列表
my_list = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]

#### 训练目标

让学员知道列表的循环和值的获取，以及列表的操作方法
'''

my_list = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]
new_list = []
for one_str in my_list:
    # if one_str[-1] =='s' or one_str[-1] =='e':
    if one_str.endswith('e') or one_str.endswith('s'):
        new_list.append(one_str)

print(new_list)