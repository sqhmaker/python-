list1 = ['一','二','三', '四']
# 增
print(list1.insert(1,"一点五"))
print(list1.append("五"))
list1.extend("liu")
print(list1)
# 删
del list1[0]
print(list1)
pop_thing = list1.pop(0)  #  有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值
print("%s已被删除" % pop_thing)

print(list1)

remove_thing = list1.remove("五")

print("%s已被删除" % remove_thing)
# 无返回值   pop 下标删除，  remove 数据删除， 都可以。
print(list1)

# list1.clear()
print(len(list1))
# 改
list1[0] = "壹"
# 查
print("nijao" in list1)
print(list1.index("三"))

num_list = [1,2,33,4,5,7,35,22,33,6,4,4]
# 操作  升序
num_list.sort()
print("排序")
print(num_list)

num_list.reverse()
print(num_list)
a_list = set(num_list)  #有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值有返回值
print(a_list)
print(list(a_list))

aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
teachers = ['Ccrolin', 'Jjanson', 'Bbeidi', 'Cclam', 'Aaj', 'Lluysi', 'Hhalou', 'Tttomoto']
teachers.sort()
aList.sort()
print("List : ", aList)
print("List : ", teachers)
print(teachers)