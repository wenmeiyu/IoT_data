from sklearn import preprocessing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib



def dis_o(oxygen,n):
    t=np.arange(len(oxygen))
    # f2=np.polyfit(t2,oxygen,3)
    # vals2=np.polyval(f2,t2)

    min_max_scaler = preprocessing.MinMaxScaler()
    oxy_minMax = min_max_scaler.fit_transform(oxygen)
    scaler = np.polyfit(t, oxy_minMax, n)
    vals_scaler = np.polyval(scaler, t)

    vals_data = {"num": t,"Oxygen": vals_scaler}
    vals_data=pd.DataFrame(vals_data)

    # print('-------', vals_data.head())
    vals = min_max_scaler.inverse_transform(vals_data)
    # print('******', vals)
    vals = vals[:, 0]


    return vals

def ph_data(ph):
    t3=np.arange(len(ph))
    f3=np.polyfit(t3,ph,5)
    vals3=np.polyval(f3,t3)

    return vals3

data2=pd.read_csv('Oxygen.csv')
time2=pd.read_csv('Oxygen.csv',usecols=['Time'])
oxygen=pd.read_csv('Oxygen.csv',usecols=['Oxygen'])
# data2=pd.read_csv('Temperature.csv')
# time2=pd.read_csv('Temperature.csv',usecols=['Time'])
# time2=list(np.array(time2))
# temp=pd.read_csv('Temperature.csv',usecols=['Temperature'])
vals_scaler=dis_o(oxygen,3)
# vals_scaler=vals_scaler[:,0]
print(vals_scaler.shape)

t2=np.arange(len(oxygen))
min_max_scaler = preprocessing.MinMaxScaler()
oxy_minMax = min_max_scaler.fit_transform(oxygen)

# val=min_max_scaler.inverse_transform(vals_scaler)

print('oxygen',oxygen.head())
print('vals_scaler',vals_scaler)
plt.figure()
#plt.subplot(211)
plt.plot(t2,oxygen,lw=1.0,label="oxygen")
#plt.figure(2)
#plt.subplot(212)
plt.ylim(0,30)
plt.plot(t2,vals_scaler,lw=2.0,label="fitting")
plt.legend(loc=0,ncol=1)
plt.show()


# min_max_scaler = preprocessing.MinMaxScaler()
# oxy_minMax = min_max_scaler.fit_transform(oxygen)
# f2_scaler=np.polyfit(t2,oxy_minMax,3)
# vals2_scaler=np.polyval(f2_scaler,t2)
# plt.figure(2)
# #plt.rcParams['savefig.dpi'] = 100
# #plt.rcParams['figure.dpi'] = 100
# plt.ylim(0,3)
# plt.plot(t2,oxy_minMax,lw=1.0,label="oxygen")
# plt.plot(t2,vals2_scaler,lw=2.0,label="fitting")
# plt.legend(loc=0,ncol=1)
#
# plt.show()



# data = np.random.uniform(0, 100, 10)[:, np.newaxis]
# mm = preprocessing.MinMaxScaler()
# mm_data = mm.fit_transform(data)
# origin_data = mm.inverse_transform(mm_data)
# print('data is ',data)
# print('after Min Max ',mm_data)
# print('origin data is ',origin_data)