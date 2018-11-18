#coding=utf-8
#2018/11/18 19:15
#author:chenyz
#数据库查询
import pymysql

def readsql():
    sql = "select * from test1"
    coon = pymysql.connect(user = "root",passwd = "root",db = "test",
                           port = 3306,host = "127.0.0.1",charset = "utf8")
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    print(info)
    coon.commit()
    cursor.close()

if __name__ == "__main__":
    readsql()
