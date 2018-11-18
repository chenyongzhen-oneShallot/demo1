#coding=utf-8
#2018/11/18 17:41
#author:chenyz

def wfile():
    try:
        file = "./" + "test"    #指定文件路径和文件名
    except IOError:
        print("没找到指定的文件")
    else:
        fp = open(file,"r+")
        fp.write("hello world")
        print(fp.read())
        fp.close()

if __name__=='__main__':
    wfile()

