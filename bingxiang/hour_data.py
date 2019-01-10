# 获取每小时第一个点的数据
import pandas as pd
import numpy as np
import datetime

file_obj = open("sheb2.txt",'r',encoding='utf-8')
file_write_obj = open("sheb2-1.txt", 'w',encoding='utf-8')
all_lines = file_obj.readlines()
t_hour=[]
i=0
result=[]
file_write_obj.write(all_lines[0])
result.append(all_lines[0])
for line in all_lines:
    ls = line.strip('\n').split('\t')
    # print(ls)
    time = c_time = datetime.datetime.strptime(ls[0], '%Y/%m/%d %H:%M')
    t_hour.append(time.hour)
    # print(t_hour)
    if(t_hour[i]!=t_hour[i-1]):
        result.append(line)
        file_write_obj.write(line)

    i=i+1

print(result)
