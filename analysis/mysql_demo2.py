# -*- coding: UTF-8 -*-
import pymysql as mdb
import sys

# 将con设定为全局连接
con = mdb.connect('localhost', 'root', '19880511', 'shuichan');

sheb_id = 1
sheb_num = 'XSCY10180101TEST0100029'
data_time = '2016/9/2 0:00'
get_time = '2016/9/1 23:59'
dis_o = 4
ph = 7.6
w_temp = 27
turbidity = 5

with con:
    # 获取连接的cursor，只有获取了cursor，我们才能进行各种操作
    cur = con.cursor()
    # # shebid,shebnum,datatime,gettime,diso,phz,wtemp,turb
    # insert = ("INSERT INTO shuichandata(sheb_id, sheb_num, data_time,get_time,dis_o,ph,w_temp,turbidity)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
    # data = (shebid,shebnum,datatime,gettime,diso,phz,wtemp,turb)
    # cur.execute(insert,data)
    # 以下插入数据
    # sql="INSERT INTO shuichandata(sheb_id, sheb_num, data_time,get_time,dis_o,ph,w_temp,turbidity)VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (sheb_id, sheb_num, data_time, get_time, dis_o, ph, w_temp, turbidity)
    sql="INSERT INTO shuichandata(sheb_id, sheb_num, data_time,get_time,dis_o,ph,w_temp,turbidity)VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (sheb_id, sheb_num, data_time, get_time, dis_o, ph, w_temp, turbidity)

    cur.execute(sql)
    # cur.execute("INSERT INTO shuichandata(sheb_id, sheb_num, data_time,get_time,dis_o,ph,w_temp,turbidity)"
    #             "VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (
    #             sheb_id, sheb_num, data_time, get_time, dis_o, ph, w_temp, turbidity))

con.close()

# # -*- coding: UTF-8 -*-
# import pymysql as mdb
# import sys
# #将con设定为全局连接
# con = mdb.connect('localhost', 'root', '19880511', 'shuichan');
#
# shebid=1;
# shebnum='XSCY10180101TEST0100029';
# datatime='2016/9/2 0:00';
# gettime='2016/9/1 23:59';
# diso=4;
# phz=7.6;
# wtemp=27;
# turb=5;
#
# with con:
#     #获取连接的cursor，只有获取了cursor，我们才能进行各种操作
#     cur = con.cursor()
#     # # shebid,shebnum,datatime,gettime,diso,phz,wtemp,turb
#     # insert = ("INSERT INTO shuichandata(sheb_id, sheb_num, data_time,get_time,dis_o,ph,w_temp,turbidity)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
#     # data = (shebid,shebnum,datatime,gettime,diso,phz,wtemp,turb)
#     # cur.execute(insert,data)
#     #以下插入数据
#     cur.execute("INSERT INTO shuichandata(sheb_id, sheb_num, data_time,get_time,dis_o,ph,w_temp,turbidity)"
#                 "VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"%(shebid,shebnum,datatime,gettime,diso,phz,wtemp,turb))
#
# con.close()


# def insert_table():
#     con = mdb.connect('localhost', 'root', '19880511', 'shuichan');
#     with con:
#         # 获取连接的cursor，只有获取了cursor，我们才能进行各种操作
#         cur = con.cursor()
#         # 以下插入了5条数据
#         cur.execute("INSERT INTO shuichandata(sheb_id, sheb_num, data_time,get_time,dis_o,ph,w_temp,turbidity) "
#                     "VALUES(1,'XSCY10180101TEST0100029','2018/9/2 0:00','2018/9/1 23:59', 4.45,7.67,26,5)")