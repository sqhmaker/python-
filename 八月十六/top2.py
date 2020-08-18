'''
使用while嵌套循环打印如下图形

```
*
* *
* * *
* * * *
* * * * *
'''
j = 1
while j <= 5:
    i = 1
    while i <= j:
        print("*", end="\t")
        i += 1
    print()
    j +=1
else:
    print("我打完了")