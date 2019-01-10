# -*- coding: UTF-8 -*-
# 安装MYSQL DB for python
#import MySQLdb as mdb
import pymysql as mdb

mysql_host = 'localhost'
mysql_db = 'shuichan'
mysql_user = 'root'
mysql_password = '19880511'
mysql_port = 3306
db = mdb.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, db=mysql_db,charset='utf8') # 连接数据库编码注意是utf8，不然中文结果输出会乱码
cursor = db.cursor()
sql = "INSERT INTO shuichandata(sheb_id, sheb_num, data_time,get_time,dis_o,ph,w_temp,turbidity) "\
          "VALUES(1,'XSCY10180101TEST0100029','2018/9/2 0:00','2018/9/1 23:59', 4.45,7.67,26,5)"
sql = sql.encode('utf-8')
cursor.execute(sql)
db.close()