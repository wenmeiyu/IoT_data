# -*- coding:utf-8 -*-
"""
import data
"""
import numpy as np
from pandas import read_csv
import csv
import json
import xlrd
import time
from dateutil import parser

# #简单读取文件并转为array进行切片 ----读取文件 分开网关
# f = open("../Data/gateway_20180518.csv", 'r')
# csvreader = csv.reader(f)
# final_list = list(csvreader)
# gate_data=np.array(final_list)
# # print(gate_data.shape[0])
# gateway1=list()
# gateway2=list()
# gateway3=list()
# for i in range(gate_data.shape[0]-1):
#     if gate_data[i][2]=='4F50425300000130':
#         gateway1.append(gate_data[i][1])
#     if gate_data[i][2] == '4F5042530000016B':
#         gateway2.append(gate_data[i][1])
#     if gate_data[i][2] == '4F50425300000111':
#         gateway3.append(gate_data[i][1])
# print(gateway1.__len__(),gateway2.__len__(),gateway3.__len__())
# print(gateway1,gateway2,gateway3)


# #简单读取文件并解析json
# cs=read_csv("/home/server/Downloads/sensor data/data_201805160926.csv")
# json_data= np.array(cs)
# # print(json_data[:,3])
# for i in range(2):
#     text=json.loads(json_data[i,3])
#     print(text['humidity'])

# # 处理json文件并且过滤时间得到要处理的数据
# csvFile = open('data_20180517.csv', 'w', newline='')
# writer = csv.writer(csvFile)
# data = xlrd.open_workbook("/home/server/Downloads/sensor data/data_201805181535.xls")
# table = data.sheets()[0]
# print(table.nrows)
# for i in range(1, table.nrows):
#     # print(table.row_values(i))
#     time_date = parser.parse(table.row_values(i)[2])
#     # print(time_date)
#     if (parser.parse('2018-05-17 00:00:00') <= time_date < parser.parse('2018-05-18 00:00:00')):
#         # print('------true')  #判断时间
#         json_data = table.row_values(i)[3]
#         # print(json_data)
#         text = json.loads(json_data)
#         # print(text)  #解析json
#         sensor_value = [text['humidity'], text['batt'], text['temperature'], table.row_values(i)[4]]
#         # print(sensor_value) #得到json值并存为list
#         new_row = table.row_values(i)[0:3] + sensor_value
#         # print(new_row)
#         writer.writerow(new_row)  # 写入
#
# csvFile.close()

# #简单写入csv文件
# csvFile2 = open('csvFile2.csv','w', newline='') # 设置newline，否则两行之间会空一行
# data=['2','5','3']
# writer = csv.writer(csvFile2)
# m = len(data)
# print(m)
# for i in range(2):
#     writer.writerow(data)
# csvFile2.close()

# # 测试时间格式相减
# time = parser.parse('2018/5/17 22:02:09') - parser.parse('2018/5/17 21:56:09')
# # time = '2018/5/17 22:02:09'-'2018/5/17 21:56:09'
# print(time)

# #测试排序代码
# # a=[parser.parse('2018/5/17 23:57:17'),parser.parse('2018/5/18 00:02:17'),parser.parse('2018/5/17 22:55:17'),parser.parse('2018/5/17 22:51:17')]
# a=['2018/5/17 23:57:17','2018/5/18 00:02:17','2018/5/17 22:55:17','2018/5/17 22:51:17']
# a.sort()
# print(a)

# #针对某一个传感器 进行排序做差 >=4min的记为0无效 否则记为1有效
# f = open("data_20180517.csv", 'r')
# csvreader = csv.reader(f)
# final_list = list(csvreader)
# sensor_data=np.array(final_list)
# # sensor=sensor_data[:,1:6]
# # print(sensor)
# sensor1=list()
# for i in range(sensor_data.shape[0]-1):
#     if sensor_data[i][1] == '3430363071377D14':
#         sensor1.append(sensor_data[i,1:6])
# print(sensor1)
#
# for i in range(sensor1.shape[0]-1):
#     if sensor_data[i][1]-sensor_data[i+1][1]>3:
#         sensor1.append(sensor_data[i,1:6])
# print(sensor1)


