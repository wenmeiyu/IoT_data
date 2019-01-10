# -*- coding:utf-8 -*-
"""
analyze data
"""
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import matplotlib.dates as mdate
from sklearn.linear_model import LinearRegression
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import adfuller
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D


# 描述统计，相关性  螺旋图
def describe_statistic():
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y/%m/%d %H:%M:%S')
    adata = pd.read_csv('../Data/dataA1_0515-19.csv', encoding='utf-8', parse_dates=['timestamp'], index_col='timestamp',
                        date_parser=dateparse)
    print(adata.head())
    print(adata.describe())  # 显示统计量 描述统计（频数，均值，标准差，分位数）
    print(adata.corr())  # 相关性分析， 不同列之间关系 humidity temperature相关性较高
    plt.style.use('seaborn-whitegrid')
    # 温度和湿度散点图  线性相关
    plt.scatter(adata['humidity'], adata['temperature'], marker='o', color='m', label='1', s=10)
    plt.show()
    # 螺旋图
    mpl.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    # z = np.linspace(-2, 2, 100)
    # r = z ** 2 + 1
    # x = r * np.sin(theta)
    # y = r * np.cos(theta)
    # print(adata['timestamp'])
    ax.plot(adata['temperature'], adata['humidity'], label='parametric curve')
    ax.legend()
    plt.show()

describe_statistic()

# 画图，x轴日期间隔显示，每天只显示一个刻度
def draw_data():
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y/%m/%d %H:%M:%S')
    adata = pd.read_csv('../Data/dataA1_0515-19.csv', encoding='utf-8', parse_dates=['timestamp'], index_col='timestamp',
                        date_parser=dateparse)
    # print(adata.head())
    # print(adata.index)
    plt.style.use('seaborn-whitegrid')
    ax = plt.axes()
    # 设置x轴为时间格式，这句非常重要，否则x轴显示的将是类似于‘736268’这样的转码后的数字格式
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))
    # 设置x轴坐标值和标签旋转45°的显示方式   画图，x轴日期间隔显示，每天只显示一个刻度
    plt.xticks(pd.date_range(adata.index[0], adata.index[-1], freq='D'), rotation=45)
    # x轴为table.index，也就是‘时间’，y轴为温度，颜色设置为红色
    ax.plot(adata.index, adata['temperature'], color='blue')
    plt.show()


# 画图，预处理
def draw_preproccess():
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y/%m/%d %H:%M:%S')
    adata = pd.read_csv('../Data/dataA1_0515-19.csv', encoding='utf-8', parse_dates=['timestamp'], index_col='timestamp',
                        date_parser=dateparse)
    plt.style.use('seaborn-whitegrid')
    plot_acf(adata['temperature'])  # ACF图   判断时间序列的平稳性
    plt.show()


# 决定起伏统计
def test_stationarity(timeseries, size):
    rolmean = pd.rolling_mean(timeseries, window=size)  # 对size个数据进行移动平均
    rol_weighted_mean = pd.ewma(timeseries, span=size)  # 对size个数据进行加权移动平均
    rolstd = pd.rolling_std(timeseries, window=size)  # 偏离原始值多少
    # 画出起伏统计
    orig = plt.plot(timeseries, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    weighted_mean = plt.plot(rol_weighted_mean, color='green', label='weighted Mean')
    std = plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)
    # 进行df测试
    print('Result of Dickry-Fuller test')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical value(%s)' % key] = value
    print(dfoutput)


# 画图，ARIMA模型
def draw_model():
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y/%m/%d %H:%M:%S')
    adata = pd.read_csv('../Data/dataA1_0515-19.csv', encoding='utf-8', parse_dates=['timestamp'], index_col='timestamp',
                        date_parser=dateparse)
    plt.style.use('seaborn-whitegrid')
    ts = adata['temperature']
    ts_log = np.log(ts)
    ts_log_diff = np.diff(ts_log)
    plt.plot(ts_log_diff, color='blue')

    # #决定起伏统计
    # test_stationarity(ts,12)   #决定起伏统计,调用test_stationarity函数

    # ARIMA模型
    model = ARIMA(ts_log, order=(2, 1, 2))
    result_ARIMA = model.fit(disp=-1)
    fitvalues = np.array(result_ARIMA.fittedvalues)
    # fitvalues = result_ARIMA.fittedvalues
    # print(ts_log_diff)
    # print(fitvalues)
    # print(result_ARIMA.fittedvalues)  #检验两条线的数据类型是否一致
    plt.plot(fitvalues, color='red')
    # plt.title('ARIMA RSS:%.4f' % sum(result_ARIMA.fittedvalues - ts_log_diff) ** 2)
    plt.show()


# ARIMA模型预测   1次差分
def predict_ARIMA():
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y/%m/%d %H:%M:%S')
    adata = pd.read_csv('../Data/dataA1_0515-19.csv', encoding='utf-8', parse_dates=['timestamp'], index_col='timestamp',
                        date_parser=dateparse)
    plt.style.use('seaborn-whitegrid')
    ts = adata['temperature']
    ts_log = np.log(ts)
    ts_log_diff = np.diff(ts_log)
    model = ARIMA(ts_log, order=(2, 1, 2))
    result_ARIMA = model.fit(disp=-1)
    predictions_ARIMA_diff = pd.Series(result_ARIMA.fittedvalues, copy=True)
    # print predictions_ARIMA_diff.head()#发现数据是没有第一行的,因为有1的延迟

    predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()
    # print predictions_ARIMA_diff_cumsum.head()

    # print(ts_log.index)   #ts_log.ix[0]=1.4816045409242156
    predictions_ARIMA_log = pd.Series(ts_log.ix[0], index=ts_log.index)
    predictions_ARIMA_log = predictions_ARIMA_log.add(predictions_ARIMA_diff_cumsum, fill_value=0)
    # print predictions_ARIMA_log.head()

    predictions_ARIMA = np.exp(predictions_ARIMA_log)
    print(type(predictions_ARIMA))
    predictions_ARIMA.to_csv('predictions_ARIMA.csv')

    plt.plot(ts)
    plt.plot(predictions_ARIMA)
    plt.title('predictions_ARIMA RMSE: %.4f' % np.sqrt(sum((predictions_ARIMA - ts) ** 2) / len(ts)))
    plt.show()


def predict_ARIMA2():
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y/%m/%d %H:%M:%S')
    adata = pd.read_csv('../Data/dataA1_0515-19.csv', encoding='utf-8', parse_dates=['timestamp'], index_col='timestamp',
                        date_parser=dateparse)
    plt.style.use('seaborn-whitegrid')
    ts = adata['temperature']
    model = ARIMA(ts, order=(2, 0, 2))
    result_ARIMA = model.fit(disp=-1)
    predict_ARIMA = pd.Series(result_ARIMA.fittedvalues, copy=True)
    # print predictions_ARIMA_diff.head()#发现数据是没有第一行的,因为有1的延迟

    print(type(predict_ARIMA))
    predict_ARIMA.to_csv('../Data/predictions_ARIMA2.csv')

    plt.plot(ts)
    plt.plot(predict_ARIMA)
    plt.title('predictions_ARIMA RMSE: %.4f' % np.sqrt(sum((predict_ARIMA - ts) ** 2) / len(ts)))
    plt.show()


# 简单线性回归
def linear_regression():
    adata = pd.read_csv('../Data/dataA1_0515-19.csv', encoding='utf-8')
    # x = np.arange(0, 226.4, 0.1)
    x=np.array(adata['humidity'])
    y = np.array(adata['temperature'])
    normalize_x = (x - np.mean(x)) / np.std(x)  # 标准化温度
    normalize_y = (y - np.mean(y)) / np.std(y)  # 标准化温度
    print('normalize_x',np.min(normalize_x))
    print('normalize_x', np.max(normalize_x))
    plt.style.use('seaborn-whitegrid')
    plt.scatter(normalize_x, normalize_y)

    model = LinearRegression(fit_intercept=True)
    model.fit(normalize_x[:, np.newaxis], normalize_y)
    xfit = np.linspace(-3, 2, 1000)
    yfit = model.predict(xfit[:, np.newaxis])
    plt.plot(xfit, yfit)
    plt.show()
    # 分组建模,测试数据
    sampleR = 0.6
    # y = adata.ix[:,2]
    # x = adata.ix[:,5]
    # nsample = len(y)
    # print(adata.ix[0, 5])
    # sampleBoundary = int(nsample * sampleR)
    # shffleIdx = range(nsample)
    # np.random.shuffle(shffleIdx)
    # train_y = y[shffleIdx[:sampleBoundary]]
    # train_x = x.ix[shffleIdx[:sampleBoundary]]
    # test_x = x.ix[shffleIdx[sampleBoundary:]]
    # test_y = y[shffleIdx[sampleBoundary:]]
    # # 线性回归模型
    # LR = sklearn.linear_model.LinearRegression()
    # LR.fit(train_x, train_y)
    # predict_y = LR.predict(test_x)
    # # 结果评估误差率，R方，回归系数，绘制图形
    # ysample = range(len(test_y))
    # error = np.linalg.norm(predict_y - test_y, ord=1) / len(test_y)
    # print("Error: %.2f" % (error))
    # print('Coefficients: \n', LR.coef_)
    # print("Residual sum of squares: %.2f" % np.mean((predict_y - test_y) ** 2))
    # print('Variance score: %.2f' % LR.score(test_x, test_y))
    # plt.plot(ysample, predict_y, 'r--', label="Predict")
    # plt.plot(ysample, test_y, 'g:', label="True")
    # plt.show()
    # # 模型预测
    # LR = sklearn.linear_model.LinearRegression()
    # LR.fit(x, y)
    # pre_y = LR.predict(x)
    # # 保存预测结果
    # res = pd.DataFrame(pre_y)
    # res.to_csv('result.csv', header=None, index=False)


# 画图实例
def draw_example():
    plt.style.use('seaborn-whitegrid')
    x = np.linspace(0, 10, 100)
    fig = plt.figure()
    # plt.plot(x,np.sin(x),'-')
    # plt.plot(x,np.cos(x),'--')
    ax = plt.axes()
    ax.plot(x, np.sin(x))
    ax.plot(x, np.cos(x), '--')
    plt.show()
    # fig.savefig('a.png')   #保存图片


def feature():
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y/%m/%d %H:%M:%S')
    adata = pd.read_csv('../Data/dataA1_0515-19.csv', encoding='utf-8', parse_dates=['timestamp'], index_col='timestamp',
                        date_parser=dateparse)
    # # 判断相关性
    t2 = np.array(adata['temperature'])[:2263]
    temperature2 = np.concatenate((np.zeros(1), t2), axis=0)  # 合并数组
    # t3 = np.array(adata['temperature'])[:2209]
    # temperature3 = np.concatenate((np.zeros(55), t3), axis=0)  # 合并数组
    # t4 = np.array(adata['temperature'])[:2261]
    # temperature4 = np.concatenate((np.zeros(3), t4), axis=0)  # 合并数组
    # t5 = np.array(adata['temperature'])[:2260]
    # temperature5 = np.concatenate((np.zeros(4), t5), axis=0)  # 合并数组
    # print('temperature2', temperature2)
    # print('000', np.zeros(30))
    adata['temperature2'] = temperature2
    # adata['temperature3'] = temperature3
    # adata['temperature4'] = temperature4
    # adata['temperature5'] = temperature5
    # print(adata.head())
    # print('corr相关性', adata.corr())

    # # 相关性画图   前1,2,3,4个时刻相关性较大
    # t3 = np.array(adata['temperature'])[:2259]
    # temperature3 = np.concatenate((np.zeros(5), t3), axis=0)  # 合并数组
    # adata['temperature3'] = temperature3
    # plt.style.use('seaborn-whitegrid')
    # ax = plt.axes()
    # ax.scatter(adata['temperature3'], adata['temperature'], marker='o', color='m', label='1', s=10)
    # plt.show()

#输出时间-温度csv文件
def output_data():
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y/%m/%d %H:%M:%S')
    adata = pd.read_csv('../Data/dataA1_0515-19.csv', encoding='utf-8', parse_dates=['timestamp'], index_col='timestamp',
                        date_parser=dateparse)
    ts = adata['temperature']
    print(type(ts))
    ts.to_csv('../Data/dataA1_0515-19_temperature.csv')


# #测试
# b=[1,2,3,4,5,6,7]
# a=np.array(b)
# print(a.cumsum())

# describe_statistic()
# draw_data()
draw_preproccess()
# draw_model()
# predict_ARIMA()
# predict_ARIMA2()
# linear_regression()
# feature()
# output_data()

# dateparse = lambda dates: pd.datetime.strptime(dates, '%Y/%m/%d %H:%M:%S')
# adata = pd.read_csv('../Data/dataA1_0515-19.csv', encoding='utf-8', parse_dates=['timestamp'], index_col='timestamp',
#                     date_parser=dateparse)
# plt.style.use('seaborn-whitegrid')
# ts = adata['temperature']
# ts_log = np.log(ts)
# ts_log_diff = np.diff(ts_log)
# plt.plot(ts_log_diff, color='blue')
#
# # #决定起伏统计
# test_stationarity(ts,12)   #决定起伏统计,调用test_stationarity函数
