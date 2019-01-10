# -*- coding: utf-8 -*-

import numpy
import matplotlib.pyplot as plt
import pandas as pd
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import datetime

# load the dataset
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y/%m/%d %H:%M:%S')
adata = pd.read_csv('../Data/dataA1_0515-19.csv', encoding='utf-8', parse_dates=['timestamp'], index_col='timestamp',
                        date_parser=dateparse)
ts=adata['temperature']
# adata = pd.read_csv('../Data/AirQualityUCI_0709.csv', encoding='utf-8')
# print(adata.describe())  # 显示统计量 描述统计（频数，均值，标准差，分位数）
# ts = adata['T']
# print(ts)
data_ts = numpy.array(ts)
print(data_ts)
for i in range(len(data_ts)):
    if data_ts[i] <= -50 or data_ts[i] >= 80:
        data_ts[i]=17.2
dataset = numpy.array(data_ts)
dataset = dataset[:, numpy.newaxis]
# 将整型变为float
dataset = dataset.astype('float32')
print('dataset',dataset.shape)
# print('dataset',dataset)
plt.plot(dataset)
plt.show()
#
cur1=datetime.datetime.now()   #获取当前系统时间

# X is the number of passengers at a given time (t) and Y is the number of passengers at the next time (t + 1).

# convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return numpy.array(dataX), numpy.array(dataY)

# fix random seed for reproducibility
numpy.random.seed(7)

# 当激活函数为 sigmoid 或者 tanh 时，要把数据正则话，此时 LSTM 比较敏感
# 设定 67% 是训练数据，余下的是测试数据
# normalize the dataset
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)

# split into train and test sets
# train_size = 1852
train_size = int(len(dataset) * 0.67)
print('train_size',train_size)
test_size = len(dataset) - train_size
# print('test_size',test_size)
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]

# X=t and Y=t+1 时的数据，并且此时的维度为 [samples, features]
# use this function to prepare the train and test datasets for modeling
look_back = 1
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)

# 投入到 LSTM 的 X 需要有这样的结构： [samples, time steps, features]，所以做一下变换
# reshape input to be [samples, time steps, features]
trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

# print('testX',testX)
# 建立 LSTM 模型：
# 输入层有 1 个input，隐藏层有 4 个神经元，输出层就是预测一个值，激活函数用 sigmoid，迭代 100 次，batch size 为 1
# create and fit the LSTM network
# model = Sequential()
# model.add(LSTM(50, input_shape=(30, look_back),return_sequences=True))
# model.add(LSTM(100, return_sequences=False))
# model.add(Dense(units=1, activation='tanh'))
# model.compile(loss='mean_squared_error', optimizer='rmsprop')  #rmsprop  adam  adagrad
# model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=1)
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='rmsprop')
model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)


# make predictions
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)

# 计算误差之前要先把预测数据转换成同一单位
# invert predictions
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform([testY])


cur2=datetime.datetime.now()   #获取当前系统时间
cur=(cur2-cur1).seconds
print("耗时",cur)
# 保存文件
pre=pd.DataFrame(testPredict)
pre.to_csv('../Data/predictions_LSTM2.csv')


def computeCorrelation(X, Y):
    xBar = numpy.mean(X)
    yBar = numpy.mean(Y)
    SSR = 0
    varX = 0
    varY = 0
    for i in range(0, len(X)):
        diffXXBar = X[i] - xBar
        diffYYBar = Y[i] - yBar
        SSR = (diffXXBar * diffYYBar)
        varX = diffXXBar ** 2
        varY = diffYYBar ** 2

    SST = math.sqrt(varX * varY)
    return SSR / SST

testR2 = computeCorrelation(testY[0], testPredict[:,0])
print('Test R2: %.16f R2' % (testR2))

# 计算 mean squared error
trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
print('Train Score: %.4f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
print('Test Score: %.4f RMSE' % (testScore))



# 画出结果：蓝色为原数据，绿色为训练集的预测值，红色为测试集的预测值
# shift train predictions for plotting
trainPredictPlot = numpy.empty_like(dataset)
trainPredictPlot[:, :] = numpy.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict

# shift test predictions for plotting
testPredictPlot = numpy.empty_like(dataset)
testPredictPlot[:, :] = numpy.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

# plot baseline and predictions
plt.plot(scaler.inverse_transform(dataset))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()

ddata=pd.DataFrame(scaler.inverse_transform(dataset))
ddata.to_csv('ddata2.csv')
traindata=pd.DataFrame(trainPredictPlot)
traindata.to_csv('traindata2.csv')
testdata=pd.DataFrame(testPredictPlot)
testdata.to_csv('testdata2.csv')
