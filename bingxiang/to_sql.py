#! /usr/bin/env python3
# ! -*- coding:utf-8 -*-
#将txt文件插入mysql数据库
import pymysql as mdb


file_obj = open("datasql.txt",'r',encoding='utf-8')
all_lines = file_obj.readlines()
# 连接数据库编码注意是utf8，不然中文结果输出会乱码
con = mdb.connect(host='210.75.252.89', port=29828, user='root', password='19880511', db='freezer',charset='utf8')

for line in all_lines:
    ls = line.strip('\n').split('\t')
    # print(ls)
    tmp = float(ls[1])
    if len(ls)==3:
        humity = float(ls[2])
        str = 'INSERT INTO freezer_data (sensor_id,data_time,temp,humidity)' \
              'VALUES(6,"%s",%f,%f);' % (ls[0], tmp, humity)
    else:
        humity = 'NULL'
        str = 'INSERT INTO freezer_data (sensor_id,data_time,temp,humidity)' \
              'VALUES(6,"%s",%f,%s);' % (ls[0], tmp, humity)


    print(str)
    with con:
        cur = con.cursor()
        cur.execute(str)

file_obj.close()

con.close()


