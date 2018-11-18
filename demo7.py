#coding=utf-8
#2018/10/28 22:13
#author:chenyz
#列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]


def square(i):
    return i*i
list = [1,2,3,4,5]
list1 = map(square,list)
print(x for x in list1 if x>10)