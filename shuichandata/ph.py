# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:13:08 2018

@author: mofashi
"""
from sklearn import preprocessing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


'''
train_time = np.array(time)
train_time_list=train_time.tolist()
list1=[str(i) for i in train_time_list]
string_time=''.join(list1)
'''

data3=pd.read_csv('PH.csv')
time3=pd.read_csv('PH.csv',usecols=['Time'])
ph=pd.read_csv('PH.csv',usecols=['PH'])
t3=np.arange(len(ph))
f3=np.polyfit(t3,ph,5)
vals3=np.polyval(f3,t3)
#plt.subplot(211)
plt.plot(t3,ph,lw=1.0,label='PH')
#plt.figure(2)
#plt.subplot(212)
plt.ylim(5,10)
plt.plot(t3,vals3,lw=2.0,label='fitting')
plt.legend(loc=0,ncol=1)
