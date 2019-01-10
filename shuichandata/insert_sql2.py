#! /usr/bin/env python3
# ! -*- coding:utf-8 -*-
import os
import csv
import pandas as pd
import numpy as np
import pymysql as mdb

# db =  mdb.connect('10.42.0.1', 'root', '19880511', 'shuichan');# 连接数据库编码注意是utf8，不然中文结果输出会乱码
# cursor = db.cursor()

file_obj = open("data2.txt",'r',encoding='utf-8')
file_write_obj = open("datasql2.txt", 'w',encoding='utf-8')
all_lines = file_obj.readlines()
for line in all_lines:
    ls = line.strip('\n').split('\t')
    print(ls)
    dis_o=float(ls[2])
    ph = float(ls[3])
    s_tmp = int(ls[4])
    zhuodu = int(ls[5])

    str='INSERT INTO shuichandata (sheb_id, sheb_num,data_time,get_time,dis_o,ph,w_temp,turbidity)' \
        'VALUES(2,"XSCY10180101TEST0100030","%s","%s",%f,%f,%d,%d);'% (ls[0], ls[1],dis_o,ph,s_tmp,zhuodu)
    # str = 'INSERT INTO tb_applicant (applicant_name, pro_area,city_area,create_date)VALUES("%s",440000,%d,now());'% (line, city_area)
    print(str)
    # cursor.execute(str)
    file_write_obj.write(str)
    file_write_obj.write('\n')

file_obj.close()

# db.close()  # 关闭数据库连