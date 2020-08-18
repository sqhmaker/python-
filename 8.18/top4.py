'''
james有一个关于爬虫的项目，他需要在一个字符串中查找python这个关键字，
当前他通过index()函数进行查找，虽然可以实现查找的需求，但是总会在
没有查找到关键字的时候报错，为什么会报错，如何优化？

#### 训练目标

1. 理解find函数和index函数的区别
'''
str = 'asdfasawvafvgad'
print(str.find('python'))
