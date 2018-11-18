#coding=utf-8
#2018/10/27 19:59
#author:chenyz

#计算1到100的和
print(sum(range(1,101)))

#改变全局变量的值
gl_a = 5
def fn():
    global gl_a
    gl_a = 4
    return gl_a

print(fn())
print(gl_a)
