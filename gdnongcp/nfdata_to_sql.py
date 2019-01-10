#! /usr/bin/env python3
# ! -*- coding:utf-8 -*-
import os
import csv
import pandas as pd
import numpy as np
import pymysql as mdb

db =  mdb.connect('193.112.113.237', 'mysql', 'mysql', 'agri');# 连接数据库编码注意是utf8，不然中文结果输出会乱码
cursor = db.cursor()

file_obj = open("lp_data.txt",'r',encoding='utf-8')
file_write_obj = open("lp.txt", 'w',encoding='utf-8')
all_lines = file_obj.readlines()
for line in all_lines:
    ls = line.strip('\n').split('\t')

    cursor.execute("SELECT id FROM tb_applicant WHERE applicant_name='"+ls[0]+"'")  # 执行SQL语句
    applicant_id = cursor.fetchone()  # 使用 fetchone() 方法获取一条applicant_id数据
    cursor.execute("SELECT type_id FROM tb_product_types WHERE type_name='" + ls[4] + "'")  # 执行SQL语句
    type_id = cursor.fetchone()  # 使用 fetchone() 方法获取一条type_id数据
    print(applicant_id)
    if applicant_id!=None and type_id != None:
        ap_id=int(applicant_id[0])
        produt_type=int(type_id[0])
        str = 'INSERT INTO tb_lp (applicant_id,product_name,certificate_code,presentation_date,annual_export_capacity,produt_type,create_date)' \
              'VALUES(%d,"%s","%s","%s",%f,%d,now());'%(ap_id,ls[1],ls[2],ls[3],float(ls[4]),produt_type)
    else:
        ap_id = 'NULL'
        produt_type = 'NULL'
        str = 'INSERT INTO tb_lp (applicant_id,product_name,certificate_code,presentation_date,annual_export_capacity,produt_type,create_date)' \
              'VALUES(%s,"%s","%s","%s",%f,%s,now());' % (ap_id, ls[1], ls[2], ls[3], float(ls[4]), produt_type)

    file_write_obj.write(str)
    file_write_obj.write('\n')
    print (str)
file_obj.close()

db.close()  # 关闭数据库连


# nfap无公害sql
# import pymysql as mdb
#
# db =  mdb.connect('193.112.113.237', 'mysql', 'mysql', 'agri');# 连接数据库编码注意是utf8，不然中文结果输出会乱码
# cursor = db.cursor()
#
# file_obj = open("nfap_type_data.txt",'r',encoding='utf-8')
# file_write_obj = open("nfap.txt", 'w',encoding='utf-8')
# all_lines = file_obj.readlines()
# for line in all_lines:
#     ls = line.strip('\n').split('\t')
#
#     cursor.execute("SELECT id FROM tb_applicant WHERE applicant_name='"+ls[0]+"'")  # 执行SQL语句
#     applicant_id = cursor.fetchone()  # 使用 fetchone() 方法获取一条applicant_id数据
#     cursor.execute("SELECT type_id FROM tb_product_types WHERE type_name='" + ls[6] + "'")  # 执行SQL语句
#     type_id = cursor.fetchone()  # 使用 fetchone() 方法获取一条type_id数据
#     print(type_id)
#     if applicant_id!=None and type_id != None:
#         ap_id=int(applicant_id[0])
#         produt_type=int(type_id[0])
#         str = 'INSERT INTO tb_nfap (applicant_id,product_name,brand,certificate_code,annual_export_capacity,produt_type,presentation_date,certificate_validity_date,create_date)' \
#               'VALUES(%d,"%s","%s","%s",%f,%d,"2016-10-16","2019-10-16",now());'%(ap_id,ls[1],ls[2],ls[3],float(ls[4]),produt_type)
#     else:
#         ap_id = 'NULL'
#         produt_type = 'NULL'
#         str = 'INSERT INTO tb_nfap (applicant_id,product_name,brand,certificate_code,annual_export_capacity,produt_type,presentation_date,certificate_validity_date,create_date)' \
#               'VALUES(%s,"%s","%s","%s",%f,%s,"2016-10-16","2019-10-16",now());'%(ap_id, ls[1], ls[2], ls[3], float(ls[4]), produt_type)
#
#     file_write_obj.write(str)
#     file_write_obj.write('\n')
#     print (str)
# file_obj.close()
#
# db.close()  # 关闭数据库连


# gf绿色sql
# import pymysql as mdb
#
# db =  mdb.connect('193.112.113.237', 'mysql', 'mysql', 'agri');# 连接数据库编码注意是utf8，不然中文结果输出会乱码
# cursor = db.cursor()
#
# file_obj = open("gf_type_data.txt",'r',encoding='utf-8')
# file_write_obj = open("gf.txt", 'w',encoding='utf-8')
# all_lines = file_obj.readlines()
# for line in all_lines:
#     ls = line.strip('\n').split('\t')
#
#     cursor.execute("SELECT id FROM tb_applicant WHERE applicant_name='"+ls[0]+"'")  # 执行SQL语句
#     applicant_id = cursor.fetchone()  # 使用 fetchone() 方法获取一条applicant_id数据
#     cursor.execute("SELECT type_id FROM tb_product_types WHERE type_name='" + ls[4] + "'")  # 执行SQL语句
#     type_id = cursor.fetchone()  # 使用 fetchone() 方法获取一条type_id数据
#     print(type_id)
#     if applicant_id!=None and type_id != None:
#         ap_id=int(applicant_id[0])
#         produt_type=int(type_id[0])
#         str = 'INSERT INTO tb_gf (applicant_id,product_name,brand,produt_type,presentation_date,certificate_validity_date,create_date)' \
#               'VALUES(%d,"%s","%s",%d,"2016-10-16","2019-10-16",now());'%(ap_id,ls[1],ls[2],produt_type)
#     else:
#         ap_id = 'NULL'
#         produt_type = 'NULL'
#         str = 'INSERT INTO tb_gf (applicant_id,product_name,brand,produt_type,presentation_date,certificate_validity_date,create_date)' \
#               'VALUES(%s,"%s","%s",%s,"2016-10-16","2019-10-16",now());' % (ap_id, ls[1], ls[2], produt_type)
#
#     file_write_obj.write(str)
#     file_write_obj.write('\n')
#     print (str)
# file_obj.close()
#
# db.close()  # 关闭数据库连

# of有机sql
# import pymysql as mdb
#
# db =  mdb.connect('193.112.113.237', 'mysql', 'mysql', 'agri');# 连接数据库编码注意是utf8，不然中文结果输出会乱码
# cursor = db.cursor()
#
# file_obj = open("of_type_data.txt",'r',encoding='utf-8')
# file_write_obj = open("of.txt", 'w',encoding='utf-8')
# all_lines = file_obj.readlines()
# for line in all_lines:
#     ls = line.strip('\n').split('\t')
#
#     cursor.execute("SELECT id FROM tb_applicant WHERE applicant_name='"+ls[0]+"'")  # 执行SQL语句
#     applicant_id = cursor.fetchone()  # 使用 fetchone() 方法获取一条applicant_id数据
#     cursor.execute("SELECT type_id FROM tb_product_types WHERE type_name='" + ls[4] + "'")  # 执行SQL语句
#     type_id = cursor.fetchone()  # 使用 fetchone() 方法获取一条type_id数据
#     print(type_id)
#     if applicant_id!=None and type_id != None:
#         ap_id=int(applicant_id[0])
#         produt_type=int(type_id[0])
#         str = 'INSERT INTO tb_of (applicant_id,product_name,product_code,produt_type,presentation_date,certificate_validity_date,create_date)' \
#               'VALUES(%d,"%s","%s",%d,"2018-10-16","2019-10-16",now());'%(ap_id,ls[1],ls[2],produt_type)
#     else:
#         ap_id = 'NULL'
#         produt_type = 'NULL'
#         str = 'INSERT INTO tb_of (applicant_id,product_name,product_code,produt_type,presentation_date,certificate_validity_date,create_date)' \
#               'VALUES(%s,"%s","%s",%s,"2018-10-16","2019-10-16",now());' % (ap_id, ls[1], ls[2], produt_type)
#
#     file_write_obj.write(str)
#     file_write_obj.write('\n')
#     print (str)
# file_obj.close()
#
# db.close()  # 关闭数据库连