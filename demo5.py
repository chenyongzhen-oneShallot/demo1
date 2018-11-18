#coding=utf-8
#2018/10/27 20:59
#author:chenyz

#列表的去重
#方法一
list = [1,2,3,1,2,2,2,1,5,6,6,4]
new_list = []
for i in list:
    if i not in new_list:
        new_list.append(i)

print(new_list)

#方法二
new_list1 = set(list)#先通过集合去重
print([x for x in new_list1])#把集合转化成列表

