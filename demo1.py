#coding=utf-8
#2018/10/26 20:44
#author:chenyz
#字符串拷贝

def str_copy(str):
    str = input("please input string:")
    str2 = ''
    if str != None:
        for str1 in str:
            str2 = str2 + str1
        print("考背后的字符串是：",str2)

if __name__ == '__main__':
    str_copy(str)
