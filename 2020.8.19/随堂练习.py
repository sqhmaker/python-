"""

"""

tuple1 = ('zhangsan',)
info = {}
info['name'] = tuple1[0]
print(info['name'])
info['name'] = 'lisi'
del info['name']

info['name'] = tuple1[0]
info.clear()
info['name'] = tuple1[0]
del info
info = {'name': tuple1[0]}
print(len(info))

info['name'] = tuple1[0]
info.keys()
info.values()
for key, value in info.items():
    print(key, value)

list1 = [22, 34, 5, 24, 55, 2]
print(max(list1))
print(min(list1))
