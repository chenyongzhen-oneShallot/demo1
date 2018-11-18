#coding=utf-8
#2018/10/28 22:09
#author:chenyz

#with操作文件
with open("readme","r+",encoding = "utf-8") as f:
    print(f.read())