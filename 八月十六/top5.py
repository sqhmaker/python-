'''
已知变量如下：

```Python
a = "itheima"
```

从键盘上输入一个字母，判断此字母 是否在变量 a 中，如果在则输出 "找到了"， 如果不在 则输出 "查无此字母"

#### 训练目标

- for...else的使用
'''
a = "itheima"
letter = input("输入一个字母：")  #字符串类型

for i in a:
    if letter == i :
        print("找到了")
        break
else:
    print("查无此字母")


