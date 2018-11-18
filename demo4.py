#coding=utf-8
#2018/10/27 20:17
#author:chenyz

#列表键值对的删除
dick = {"name":"jock","age":22}
del dick["name"]
print(dick)

#两个列表的合并
dick2 = {"name":"jock"}
dick.update(dick2)
print(dick)