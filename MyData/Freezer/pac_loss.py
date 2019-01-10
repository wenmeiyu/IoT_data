import pandas as pd
import numpy as np
import datetime


data = pd.read_csv('adata.csv', encoding='utf-8')
data_time = data['time']
# print(data_time.head())
# print(len(data_time))
# print(type(data_time))

time=[]
shouid_num=[]
real_num=[]
loss_rate=[]

# for i in range(len(data_time)):
#

for item in data_time[0:7]:
    # print(item)
    c_time = datetime.datetime.strptime(item, '%Y-%m-%d %H:%M')
    # print(type(c_time))
    c_year = c_time.year
    c_month = c_time.month
    c_day = c_time.day
    c_hour = c_time.hour
    print(c_year,c_month,c_day,c_hour)

