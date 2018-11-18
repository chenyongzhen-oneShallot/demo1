#coding=utf-8
#2018/10/29 21:40
#author:chenyz

#字典根据键从小到大排序dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
#i[0]表示键，i[1]表示值
list = sorted(dict.items(),key = lambda i:i[0],reverse = False)
new_dict={}
for i in list:
    new_dict[i[0]] = i[1]

print(new_dict)

