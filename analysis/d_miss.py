# -*- coding:utf-8 -*-
"""
data analyze 20180828
"""

import xlrd
import os

print ("当前工作目录 : %s" % os.getcwd())
data = xlrd.open_workbook("data_os_20180828.xls") # 打开xls文件
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows      # 获取表的行数
print("nrows",nrows)
