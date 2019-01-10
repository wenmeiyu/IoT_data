# -*- coding: UTF-8 -*-
# 安装MYSQL DB for python
# 验证链接数据库成功与否
#import MySQLdb as mdb
import pymysql as mdb
con = None
try:
    # 连接mysql的方法：connect(host='localhost 192.168.200.16 172.20.117.167',user='root',passwd='root',db='test',port=3306)
    # con = mdb.connect('192.168.200.25', 'root','19880511', 'shuichan',2004)
    # con = mdb.connect(host='10.42.0.1', port=3306, user='root', password='19880511', db='freezer', charset='utf8')
    con = mdb.connect(host='210.75.252.89', port=29828, user='root', password='19880511', db='freezer', charset='utf8')
    # 所有的查询，都在连接con的一个模块cursor上面运行的
    cur = con.cursor()
    # 执行一个查询
    cur.execute("SELECT VERSION()")
    # 取得上个查询的结果，是单个结果
    data = cur.fetchone()
    print("Database version : %s " % data)
finally:
    if con:
        # 无论如何，连接记得关闭
        con.close()
