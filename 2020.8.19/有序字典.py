import collections

print("Regular dictionary")
d = {}
d['a'] = 'A'
d['c'] = 'C'
d['b'] = 'B'
for k, v in d.items():
    print(k, v)

print("\nOrder dictionary")
d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['c'] = 'C'
d1['1'] = '1'
d1['b'] = 'B'
d1['2'] = '2'

for k, v in d1.items():
    print(k, v)
'''
输出：
Regular dictionary
a A
c C
b B

Order dictionary
a A
b B
c C
1 1
2 2
'''
