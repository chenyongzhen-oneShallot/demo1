#coding=utf-8
#2018/10/26 20:58
#author:chenyz
#字符串反转

def str_reverse(str):
    str = input()
    str2 = ''
    for str1 in str:
        str2 = str1 + str2
    print(str2)

if __name__== '__main__':
    str_reverse(str)