'''
字典的每个元素由2部分组成，键:值。例如 'name':'班长' ,'name'为键，'班长'为值
                        key : value
info['sex'] = real_sex   没有这个键，补充；有，修改

'''

# info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}
#
# # real_sex = input("请输入性别：")
# # add_age = input("请补充年龄：")
# del info['address']
# info.clear()
# info['id'] = 66
# # info['sex'] = real_sex
# # info['age'] = add_age
# print(info)
# print('id值为：%d' % info['id'])
#
# print(info['name'])
# print(info['address'])
# print(info['id'])
# print(info['sex'])
# # print(info['age'])
# print(info.get('age',18))
# print(info.get('sex'))
# x = info.get('sex')
# print(x)
info = {'name': 'monitor', 'sex': 'f', 'address': 'China'}
print('清空前,%s' % info)
info.clear()
print('清空后,%s' % info)

#
# for key, value in info:
#     print(key, value)
print(info.values())
print(info.keys())
print(info.items())
print(len(info))

# 打印我的第一个字典
web_set = {'name': 'bilibili', 'age': 10, 2: 33}
print(web_set.items())

av_catalog = {
    '欧美': {
        'www.youporn.com': ['很多免费的，世界最大', '质量一般'],
        'www.pornhub.com': ['很多免费的，很大', '质量比youpirn高点'],
        'letmedothistoyou.com': ['多事自拍，高质量图片很多', '资源不多，更新慢'],
        'x-art.com': ['质量很高，真的很高', '全部收费，屌丝请绕行']
    },
    '日韩': {
        'tokyo': ['质量很高，个人已经不喜欢日韩范了', '听说是收费的']
    },
    '大陆': {
        '1024': ['全部免费，好人一生平安', '服务器在国外，慢']
    }
}
av_catalog['欧美']['www.youporn.com'][1] = '高高清清'  # 修改指定的值，首先找到大的字典里的键，然后在找到资格字典里套的这个字典的键，然后在找到要修改的这个内容在列表的位置。
print(av_catalog)

for i, v in av_catalog['欧美'].items():
    print(i, v)
for i in av_catalog['欧美'].keys():
    print(i)
print('--------------------------------------------------------------')
OrderDict
