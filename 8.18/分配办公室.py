'''
需求:  8个老师随机分配到三个办公室

要求：  列表嵌套

思路：  建立老师数组（列表）（因为比较多，不一个一个赋值），
       建立办公室列表
       random分配

'''

import random
teachers = ['Ccrolin','Jjanson','Bbeidi','Cclam','Aaj','Lluysi','Hhalou','Tttomoto']
teachers.sort()
print(teachers)
offices = [[],[],[]]

'''
放进去之后

另起一个

打印每一个房间里的人数、老师
'''

for teacher in teachers :
    room_number = random.randint(0,2)
    offices[room_number].append(teacher)
print(offices)
i = 0
for office in offices:
    print(f"{i}号房有{len(office)}人，分别是")
    for name in office:
        print(name)
    i += 1

