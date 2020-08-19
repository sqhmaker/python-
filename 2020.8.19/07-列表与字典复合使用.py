"""
然后小明一共有8000块钱，那么他能不能买下这所有商品？
如果能，请输出“能”，否则输出“不能”

#### 训练目标

if判断语句的复习使用
列表与字典的复合使用
遍历列表与遍历字典的使用

思路：
1 遍历所有商品相加，判断是否超出8000
两层循环遍历

"""
product = [
    {"name": "电脑", "price": 7000},
    {"name": "鼠标", "price": 30},
    {"name": "usb电动小风扇", "price": 20},
    {"name": "遮阳伞", "price": 50},
]
sum_money = 0
for goods in product:
    for key, value in goods.items():
        if key == 'price':
            sum_money += value
print(sum_money)
if sum_money <= 8000:
    print('能')

