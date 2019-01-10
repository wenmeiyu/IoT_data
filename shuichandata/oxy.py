# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:46:38 2018

@author: mofashi
"""
from sklearn import preprocessing   
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

data2=pd.read_csv('Oxygen.csv')
time2=pd.read_csv('Oxygen.csv',usecols=['Time'])
oxygen=pd.read_csv('Oxygen.csv',usecols=['Oxygen'])
t2=np.arange(len(oxygen))
f2=np.polyfit(t2,oxygen,3)
vals2=np.polyval(f2,t2)
plt.figure(1)
#plt.subplot(211)
plt.plot(t2,oxygen,lw=1.0,label="oxygen")
#plt.figure(2)
#plt.subplot(212)
plt.ylim(0,30)
plt.plot(t2,vals2,lw=2.0,label="fitting")
plt.legend(loc=0,ncol=1)


min_max_scaler = preprocessing.MinMaxScaler()  
oxy_minMax = min_max_scaler.fit_transform(oxygen)  
f2_scaler=np.polyfit(t2,oxy_minMax,3)
vals2_scaler=np.polyval(f2_scaler,t2)
plt.figure(2)
#plt.rcParams['savefig.dpi'] = 100
#plt.rcParams['figure.dpi'] = 100
plt.ylim(0,3)
plt.plot(t2,oxy_minMax,lw=1.0,label="oxygen")
plt.plot(t2,vals2_scaler,lw=2.0,label="fitting")
plt.legend(loc=0,ncol=1)
