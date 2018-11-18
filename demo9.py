#coding=utf-8
#2018/10/29 20:32
#author:chenyz

#s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"
s = set(s)
s = list(s)
s.sort()
res = "".join(s)
print(res)






