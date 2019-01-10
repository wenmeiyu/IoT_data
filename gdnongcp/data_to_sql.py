#! /usr/bin/env python3
# ! -*- coding:utf-8 -*-
# ------------
# 一个把txt文件转化成sql语句的小程序，还可以通过查询mysql添加关联对象数据
# -----------
import os
import csv
import pandas as pd
import numpy as np
import pymysql as mdb

db =  mdb.connect('193.112.113.237', 'mysql', 'mysql', 'agri');# 连接数据库编码注意是utf8，不然中文结果输出会乱码
cursor = db.cursor()

file_obj = open("ap_data.txt",'r',encoding='utf-8')
file_write_obj = open("applicant.txt", 'w',encoding='utf-8')
all_lines = file_obj.readlines()
for line in all_lines:
    line=line.strip('\n')
    area_name=line[0:3]

    cursor.execute("SELECT id FROM tb_area WHERE NAME='"+area_name+"'")  # 执行SQL语句
    area_id = cursor.fetchone()  # 使用 fetchone() 方法获取一条数据
    if area_id!=None:
        city_area=int(area_id[0])
        str = 'INSERT INTO tb_applicant (applicant_name, pro_area,city_area,create_date)VALUES("%s",440000,%d,now());'% (line, city_area)
    else:
        city_area='NULL'
        str = 'INSERT INTO tb_applicant (applicant_name, pro_area,city_area,create_date)VALUES("%s",440000,%s,now());' % (line, city_area)

    file_write_obj.write(str)
    file_write_obj.write('\n')
    print (type(city_area))
file_obj.close()

db.close()  # 关闭数据库连

# tgcode ="dafafadfaf"
# result = "window.config = '%s';" % (tgcode)
# print(result)

# with open("test.csv","w") as csvfile:
#     writer = csv.writer(csvfile) #先写入columns_name
#     writer.writerow(["index","a_name","b_name"]) #写入多行用writerows
#     writer.writerows([[0,1,3],[1,2,3],[2,3,4]])


# file=pd.read_csv('ap_data.csv',encoding='utf-8')
# data=np.array(file['applicant_name'])
# print (data)
# with open("applicant.csv","w") as csvfile:
#     for i in range(len(file)):
#         writer = csv.writer(csvfile)
#         writer.writerow(['INSERT INTO tb_applicant (applicant_name, pro_area,city_area,create_date)VALUES("'+data[i]])
#         print (i)