#coding=utf-8
#2018/10/28 22:29
#author:chenyz

#python中生成随机整数、随机小数、0-1之间小数方法

import random
import numpy
#生成1到10之间的正数
print(random.randint(1,10))
#生成5个随机小数
print(numpy.random.randn(5))

#生成0到1之间的小数
print(random.random())