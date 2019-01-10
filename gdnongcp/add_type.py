#! /usr/bin/env python3

# ! -*- coding:utf-8 -*-

# type_data.txt-type.txt  临时表
# file_obj = open("type_data.txt",'r',encoding='utf-8')
# file_write_obj = open("type.txt", 'w',encoding='utf-8')
# all_lines = file_obj.readlines()
# for line in all_lines:
#     ls = line.strip('\n').split('\t')
#     str = 'INSERT INTO tmp (industry_type,product_type,product_name)VALUES("%s","%s","%s");'% (ls[0],ls[1],ls[2] )
#     file_write_obj.write(str)
#     file_write_obj.write('\n')
#     print(str)
# file_obj.close()
# ------------
# 一个把txt文件转化成sql语句的小程序，还可以通过查询mysql添加关联对象数据
# -----------

# # 增加产品类型列
# import pymysql as mdb
#
# db =  mdb.connect('193.112.113.237', 'mysql', 'mysql', 'agri');# 连接数据库编码注意是utf8，不然中文结果输出会乱码
# cursor = db.cursor()
#
# file_obj = open("nfap_data.txt",'r',encoding='utf-8')
# file_write_obj = open("nfap_type_data.txt", 'w',encoding='utf-8')
# all_lines = file_obj.readlines()
# for line in all_lines:
#     ls = line.strip('\n').split('\t')
#     pro_name=ls[1]
#
#     cursor.execute("SELECT industry_type,product_type FROM tmp WHERE product_name='"+pro_name+"'")  # 执行SQL语句
#     pro_list = cursor.fetchone()  # 使用 fetchone() 方法获取一条数据
#     if pro_list!=None:
#         ind_type=pro_list[0]
#         pro_type=pro_list[1]
#         str = line.strip('\n') + '\t' +ind_type + '\t' + pro_type
#     else:
#         ind_type = 'NULL'
#         pro_type = 'NULL'
#         str = line.strip('\n') + '\t' + ind_type + '\t' + pro_type
#     file_write_obj.write(str)
#     file_write_obj.write('\n')
#     print(str)
# file_obj.close()
# db.close()  # 关闭数据库连

# # 行转列，将一个公司的多个产品转化为一对一
# file_obj = open("gf_data.txt",'r',encoding='utf-8')
# file_write_obj = open("gf_data1.txt", 'w',encoding='utf-8')
# all_lines = file_obj.readlines()
# for line in all_lines:
#     ls = line.strip('\n').split('\t')
#     pro_name_ls=ls[1].replace('、',',').split(',')
#     for i in range(len(pro_name_ls)):
#         str=ls[0] + '\t' +pro_name_ls[i] + '\t' + ls[2]
#         file_write_obj.write(str)
#         file_write_obj.write('\n')
#
#     print(pro_name_ls)
# file_obj.close()


# 增加产品类型列
import pymysql as mdb

db =  mdb.connect('193.112.113.237', 'mysql', 'mysql', 'agri');# 连接数据库编码注意是utf8，不然中文结果输出会乱码
cursor = db.cursor()

file_obj = open("of_data.txt",'r',encoding='utf-8')
file_write_obj = open("of_type_data.txt", 'w',encoding='utf-8')
all_lines = file_obj.readlines()
for line in all_lines:
    ls = line.strip('\n').split('\t')
    pro_name=ls[1]

    cursor.execute("SELECT industry_type,product_type FROM tmp WHERE product_name='"+pro_name+"'")  # 执行SQL语句
    pro_list = cursor.fetchone()  # 使用 fetchone() 方法获取一条数据
    if pro_list!=None:
        ind_type=pro_list[0]
        pro_type=pro_list[1]
        str = line.strip('\n') + '\t' +ind_type + '\t' + pro_type
    else:
        ind_type = 'NULL'
        pro_type = 'NULL'
        str = line.strip('\n') + '\t' + ind_type + '\t' + pro_type
    file_write_obj.write(str)
    file_write_obj.write('\n')
    print(str)
file_obj.close()
db.close()  # 关闭数据库连