# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:46:13 2018

@author: mofashi
"""
from sklearn import preprocessing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import matplotlib as plt

data=pd.read_csv('Temperature.csv')
time=pd.read_csv('Temperature.csv',usecols=['Time'])
temperature=pd.read_csv('Temperature.csv',usecols=['Temperature'])
t=np.arange(len(temperature))
f=np.polyfit(t,temperature,4)
vals=np.polyval(f,t)
#plt.rcParams['savefig.dpi'] = 100
#plt.rcParams['figure.dpi'] = 100
plt.figure(1)
#plt.subplot(211)
plt.ylim(0,40)
plt.plot(t,temperature,lw=1.0,label="temperature")
#plt.figure(2)
#plt.subplot(212)
plt.ylim(0,40)
plt.plot(t,vals,lw=2.0,label="fitting")
plt.legend(loc=0,ncol=1)

min_max_scaler = preprocessing.MinMaxScaler()  
tem_minMax = min_max_scaler.fit_transform(temperature)  
f_scaler=np.polyfit(t,tem_minMax,4)
vals_scaler=np.polyval(f_scaler,t)
plt.figure(2)
plt.ylim(0,3)
plt.plot(t,tem_minMax,lw=1.0,label="temperature")
plt.plot(t,vals_scaler,lw=2.0,label="fitting")
plt.legend(loc=0,ncol=1)
